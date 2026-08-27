import copy
from datetime import date, timedelta
import json
from pathlib import Path
import tempfile
import unittest

from inventory_checker import A, B, C, DEAD, DEFAULT_CONFIG, analyze, classify, new_state, run, step

class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.cfg = copy.deepcopy(DEFAULT_CONFIG)
        self.cfg.update(item_count=12, a_count=2, b_count=3)
        self.day = date(2026, 8, 27)
        self.state = new_state(self.day, self.cfg)
        self.item = self.state['items'][0]
        self.item.update(on_hand=0, orders=[], lead_days=7, lead_sd_days=1)
        self.item['history'] = [{'date': (self.day-timedelta(days=n)).isoformat(), 'demand': 10, 'sold': 10} for n in reversed(range(90))]

    def result(self, item=None, label=A):
        return analyze(item or self.item, label, 900, self.day, self.cfg)

    def test_lead_time_increases_stock(self):
        short = self.result()
        self.item['lead_days'] = 60
        long = self.result()
        self.assertGreater(long['reorder_point'], short['reorder_point'])
        self.assertGreater(long['suggested_order'], short['suggested_order'])

    def test_variable_lead_increases_safety(self):
        before = self.result()['safety_stock']
        self.item['lead_sd_days'] = 10
        self.assertGreater(self.result()['safety_stock'], before)

    def test_variability_and_class_policy(self):
        self.item['history'][-1]['demand'] = 150
        self.assertGreater(self.result(label=A)['safety_stock'], self.result(label=C)['safety_stock'])

    def test_stock_formula(self):
        result = self.result()
        self.assertEqual(result['safety_stock'], 21)
        self.assertEqual(result['reorder_point'], 101)
        self.assertEqual(result['target_stock'], 241)

    def test_open_orders_prevent_duplicate_but_warn_late(self):
        self.item.update(on_hand=10, orders=[{'qty':1000, 'due':'2026-12-01'}])
        result = self.result()
        self.assertEqual(result['suggested_order'], 0)
        self.assertEqual(result['health'], 'Lead-time risk')
        self.assertEqual(result['projected_gap_in_days'], 2)

    def test_timely_receipt_prevents_gap(self):
        self.item.update(on_hand=10, orders=[{'qty':1000, 'due':'2026-08-28'}])
        self.assertIsNone(self.result()['projected_gap_in_days'])

    def test_dead_stock_not_reordered(self):
        self.assertEqual(self.result(label=DEAD)['suggested_order'], 0)

    def test_moq_pack(self):
        self.item.update(moq=500, pack_size=12)
        self.assertEqual(self.result()['suggested_order'], 504)

    def test_class_boundaries_and_zero_sales(self):
        items = []
        for n in range(8):
            item = copy.deepcopy(self.item)
            item.update(sku=f'ITEM-{n:04d}', history=[{'date': self.day.isoformat(), 'sold': 7-n}])
            items.append(item)
        labels, _ = classify(items, self.day, self.cfg)
        self.assertEqual(list(labels.values()), [A,A,B,B,B,C,C,DEAD])
        items[0]['core_product'] = False
        self.assertEqual(classify(items, self.day, self.cfg)[0]['ITEM-0000'], 'Non-core')

    def test_same_date_idempotent_and_catchup(self):
        with tempfile.TemporaryDirectory() as td:
            one, two = Path(td)/'one', Path(td)/'two'
            run(one, self.day, self.cfg)
            before = (one/'data/state.json').read_bytes()
            report = (one/'reports/latest.json').read_bytes()
            self.assertFalse(run(one, self.day, self.cfg))
            self.assertEqual(before, (one/'data/state.json').read_bytes())
            self.assertEqual(report, (one/'reports/latest.json').read_bytes())
            run(two, self.day, self.cfg)
            for n in range(1, 4):
                run(one, self.day + timedelta(days=n), self.cfg)
            run(two, self.day + timedelta(days=3), self.cfg)
            self.assertEqual((one/'data/state.json').read_bytes(), (two/'data/state.json').read_bytes())
            with self.assertRaises(ValueError):
                run(one, self.day, self.cfg)

    def test_stock_conservation_and_receipts(self):
        before = {i['sku']: i['on_hand'] for i in self.state['items']}
        self.state['items'][0]['orders'] = [{'qty': 50, 'due': self.day.isoformat()}]
        step(self.state, self.day)
        for i in self.state['items']:
            h = i['history'][-1]
            self.assertEqual(i['on_hand'], before[i['sku']] + h['received'] - h['sold'])
            self.assertEqual(h['demand'], h['sold'] + h['lost'])
            self.assertGreaterEqual(i['on_hand'], 0)
            self.assertTrue(all(o['due'] > self.day.isoformat() for o in i['orders']))

    def test_no_financial_or_real_identifiers(self):
        step(self.state, self.day)
        text = json.dumps(self.state).lower()
        for forbidden in ('cost', 'price', 'dollar', 'mcs', 'sage', 'vendor'):
            self.assertNotIn(forbidden, text)
        self.assertTrue(all(i['sku'].startswith('ITEM-') for i in self.state['items']))

if __name__ == '__main__':
    unittest.main()
