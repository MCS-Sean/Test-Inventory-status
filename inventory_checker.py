"""Synthetic-only inventory simulation. Python 3.11+, standard library only."""
import argparse
import calendar
from collections import Counter
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path
import random
import statistics

A, B, C, DEAD = 'A - Top Movers', 'B - Core Products', 'C - Slow Moving', 'Dead Inv'
DEFAULT_CONFIG = {
    'seed': 173, 'item_count': 160,
    'a_count': 25, 'b_count': 75,
    'forecast_days': 90, 'review_days': 1,
    'excess_target_multiple': 1.5,
    'policies': {
        A: {'z': 2.05, 'cycle_days': 14},
        B: {'z': 1.65, 'cycle_days': 21},
        C: {'z': 1.28, 'cycle_days': 30},
        DEAD: {'z': 0, 'cycle_days': 0},
    },
}

def validate_config(cfg):
    for key in ('seed', 'item_count', 'a_count', 'b_count', 'forecast_days', 'review_days'):
        if type(cfg[key]) is not int or cfg[key] < (1 if key in ('item_count', 'forecast_days', 'review_days') else 0):
            raise ValueError(f'Invalid {key}')
    if cfg['forecast_days'] > 365 or cfg['excess_target_multiple'] <= 1:
        raise ValueError('forecast_days must be <=365 and excess_target_multiple >1')
    for label in (A, B, C, DEAD):
        p = cfg['policies'][label]
        if p['z'] < 0 or p['cycle_days'] < 0:
            raise ValueError('Policies cannot be negative')


def rng_for(seed, *parts):
    key = '|'.join(map(str, (seed,) + parts)).encode()
    return random.Random(int.from_bytes(hashlib.sha256(key).digest()[:8], 'big'))


def demand_for(item, day, seed):
    rng = rng_for(seed, item['sku'], day.isoformat(), 'demand')
    mode, base = item['behavior'], item['base_daily_demand']
    if mode == 'inactive':
        return 0
    if mode == 'intermittent':
        return rng.randint(1, max(2, round(base * 15))) if rng.random() < 0.12 else 0
    seasonal = 1 + 0.65 * math.sin(2 * math.pi * day.timetuple().tm_yday / 365.25)
    mean = base * (seasonal if mode == 'seasonal' else 1)
    return max(0, round(rng.gauss(mean, max(0.8, mean * 0.45))))


def year_start(day):
    # Exclude the same date in the preceding year; handle February 29.
    prior = day.replace(year=day.year - 1, day=min(day.day, calendar.monthrange(day.year - 1, day.month)[1]))
    return prior + timedelta(days=1)


def classify(items, day, cfg):
    start = year_start(day).isoformat()
    totals = {i['sku']: sum(h['sold'] for h in i['history'] if start <= h['date'] <= day.isoformat()) for i in items}
    ranked = sorted((i for i in items if i['core_product'] and totals[i['sku']] > 0),
                    key=lambda i: (-totals[i['sku']], i['sku']))
    result = {i['sku']: DEAD if totals[i['sku']] == 0 else 'Non-core' for i in items}
    for rank, item in enumerate(ranked):
        result[item['sku']] = A if rank < cfg['a_count'] else B if rank < cfg['a_count'] + cfg['b_count'] else C
    return result, totals


def analyze(item, label, sold_12m, day, cfg):
    history = item['history'][-cfg['forecast_days']:]
    demands = [h['demand'] for h in history]
    mean = statistics.mean(demands) if demands else 0.0
    sd = statistics.pstdev(demands) if demands else 0.0
    lead, lead_sd = item['lead_days'], item['lead_sd_days']
    policy = cfg['policies'].get(label, cfg['policies'][C])
    z = policy['z']
    protection = lead + cfg['review_days']
    safety = math.ceil(z * math.sqrt(protection * sd ** 2 + mean ** 2 * lead_sd ** 2))
    reorder = math.ceil(mean * protection + safety)
    target = math.ceil(mean * (protection + policy['cycle_days']) + safety)
    on_order = sum(o['qty'] for o in item['orders'])
    position = item['on_hand'] + on_order
    manual = label in (DEAD, 'Non-core')
    # Demand is lost rather than backordered; no hidden allocations/backlog.
    suggested = max(0, target - position) if position <= reorder and mean > 0 and not manual else 0
    if suggested:
        suggested = math.ceil(max(item['moq'], suggested) / item['pack_size']) * item['pack_size']
    # Test projected balances daily through a conservative lead-time horizon.
    horizon = math.ceil(lead + z * lead_sd)
    balance, gap = float(item['on_hand']), None
    for offset in range(1, horizon + 1):
        arrival = (day + timedelta(days=offset)).isoformat()
        balance += sum(o['qty'] for o in item['orders'] if o['due'] == arrival)
        balance -= mean
        if balance < -1e-9 and gap is None:
            gap = offset
    coverage = round(item['on_hand'] / mean, 1) if mean > 0 else None
    excess = max(0, item['on_hand'] - target)
    if label == DEAD:
        health = 'Dead inventory' if item['on_hand'] else 'Inactive / no stock'
        action = 'Manual review; do not replenish automatically'
    elif label == 'Non-core':
        health, action = 'Non-core review', 'Manual review'
    elif mean == 0:
        health, action = 'Dormant demand', 'Review inactivity; do not replenish automatically'
    elif item['on_hand'] == 0:
        health, action = 'Stockout', 'Expedite open supply or review emergency replenishment'
    elif gap is not None:
        health, action = 'Lead-time risk', 'Review receipt dates; expedite supply before projected gap'
    elif suggested:
        health, action = 'Reorder', 'Place suggested replenishment'
    elif item['on_hand'] > target * cfg['excess_target_multiple']:
        health, action = 'Excess', 'Pause purchases; review redistribution or demand'
    else:
        health, action = 'Healthy', 'Monitor'
    return {
        'sku': item['sku'], 'name': item['name'], 'movement_class': label,
        'behavior': item['behavior'], 'sold_last_12_months': sold_12m,
        'on_hand': item['on_hand'], 'on_order': on_order, 'inventory_position': position,
        'lead_days': lead, 'lead_sd_days': lead_sd, 'lead_time_demand': round(mean * lead, 2),
        'mean_daily_demand': round(mean, 3), 'daily_demand_sd': round(sd, 3),
        'safety_stock': safety, 'reorder_point': reorder, 'target_stock': target,
        'coverage_days': coverage, 'lead_time_coverage_ratio': round(coverage / lead, 2) if coverage is not None else None,
        'projected_gap_in_days': gap, 'suggested_order': suggested, 'excess_above_target': excess,
        'health': health, 'action': action,
    }


def new_state(day, cfg):
    items = []
    first = day - timedelta(days=366)
    for n in range(1, cfg['item_count'] + 1):
        sku = f'ITEM-{n:04d}'
        rng = rng_for(cfg['seed'], sku, 'catalog')
        behavior = rng.choices(['steady', 'seasonal', 'intermittent', 'inactive'], [40, 20, 25, 15])[0]
        base = round(rng.uniform(0.4, 18), 2)
        lead = rng.choice([7, 14, 30, 45, 60, 90])
        item = {'sku': sku, 'name': f'Generic Component {n:04d}', 'core_product': True,
                'behavior': behavior, 'base_daily_demand': base,
                'lead_days': lead, 'lead_sd_days': max(1, round(lead * 0.2)),
                'moq': rng.choice([1, 5, 10]), 'pack_size': rng.choice([1, 5]),
                'on_hand': 0, 'orders': [], 'history': []}
        for offset in range(366):
            d = first + timedelta(days=offset)
            demand = demand_for(item, d, cfg['seed'])
            item['history'].append({'date': d.isoformat(), 'demand': demand, 'sold': demand,
                                    'lost': 0, 'received': 0})
        # The pre-simulation history assumes unconstrained synthetic fulfillment.
        avg = statistics.mean(h['demand'] for h in item['history'][-90:])
        factor = rng.choice([0.1, 0.4, 1.0, 1.5, 4.0])
        item['on_hand'] = max(0, round(avg * (lead + 21) * factor)) if behavior != 'inactive' else rng.randint(0, 100)
        items.append(item)
    return {'schema_version': 1, 'synthetic_only': True, 'config': cfg,
            'last_date': (day - timedelta(days=1)).isoformat(), 'items': items}


def step(state, day):
    cfg = state['config']
    for item in state['items']:
        received = sum(o['qty'] for o in item['orders'] if o['due'] <= day.isoformat())
        item['orders'] = [o for o in item['orders'] if o['due'] > day.isoformat()]
        item['on_hand'] += received
        demand = demand_for(item, day, cfg['seed'])
        sold = min(item['on_hand'], demand)
        item['on_hand'] -= sold
        item['history'].append({'date': day.isoformat(), 'demand': demand, 'sold': sold,
                                'lost': demand - sold, 'received': received})
        item['history'] = item['history'][-366:]
    classes, totals = classify(state['items'], day, cfg)
    rows = []
    for item in state['items']:
        row = analyze(item, classes[item['sku']], totals[item['sku']], day, cfg)
        row['simulated_order_placed'] = row['suggested_order']
        row['new_order_due'] = None
        if row['suggested_order']:
            rng = rng_for(cfg['seed'], item['sku'], day.isoformat(), 'lead')
            actual_lead = max(1, round(rng.gauss(item['lead_days'], item['lead_sd_days'])))
            due = (day + timedelta(days=actual_lead)).isoformat()
            item['orders'].append({'qty': row['suggested_order'], 'due': due})
            row['new_order_due'] = due
        rows.append(row)
    state['last_date'] = day.isoformat()
    return rows


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True, allow_nan=False) + '\n', encoding='utf-8')
    tmp.replace(path)


def write_reports(root, day, rows):
    counts = dict(sorted(Counter(r['health'] for r in rows).items()))
    write_json(root / 'reports/latest.json', {'synthetic_only': True, 'date': day.isoformat(),
        'snapshot': 'After demand, before today\'s simulated orders; new orders shown separately',
        'health_counts': counts, 'items': rows})
    lines = ['# Synthetic Inventory Health', '', f'**Simulation date: {day}**', '',
             'All products, quantities, demand, and supplier lead times are fictional. No financial fields.', '',
             'Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.', '',
             '## Health summary', '', '| Status | Items |', '|---|---:|']
    lines += [f'| {k} | {v} |' for k, v in counts.items()]
    lines += ['', '## Movement classes', '', '| Class | Items |', '|---|---:|']
    lines += [f'| {label} | {sum(r["movement_class"] == label for r in rows)} |' for label in (A, B, C, DEAD)]
    lines += ['', '## Stocking detail', '',
              'Longer lead times increase demand exposure and stock targets. Incoming orders count toward inventory position, but late receipts can still create a stockout risk.', '',
              '| Item | Class | Health | On hand | On order | Lead days | Cover days | Safety | Reorder | Target | New order | Gap in days |',
              '|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        cover = r['coverage_days'] if r['coverage_days'] is not None else 'N/A'
        gap = r['projected_gap_in_days'] if r['projected_gap_in_days'] is not None else '—'
        lines.append(f'| {r["sku"]} | {r["movement_class"]} | {r["health"]} | {r["on_hand"]} | {r["on_order"]} | {r["lead_days"]} | {cover} | {r["safety_stock"]} | {r["reorder_point"]} | {r["target_stock"]} | {r["simulated_order_placed"]} | {gap} |')
    (root / 'reports/latest.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def run(root, day, cfg):
    validate_config(cfg)
    path = root / 'data/state.json'
    state = json.loads(path.read_text(encoding='utf-8')) if path.exists() else new_state(day, cfg)
    if state.get('schema_version') != 1 or state.get('synthetic_only') is not True:
        raise ValueError('Only version 1 synthetic state is supported')
    if state['config'] != cfg:
        raise ValueError('Configuration changed: use a new output directory for a fresh simulation')
    last = date.fromisoformat(state['last_date'])
    if day < last:
        raise ValueError('Cannot run backward; use a new output directory')
    if day == last:
        # Rebuild reports after an interrupted write without repeating simulation.
        write_reports(root, day, state['latest_rows'])
        return False
    current = last + timedelta(days=1)
    while current <= day:
        rows = step(state, current)
        current += timedelta(days=1)
    state['latest_rows'] = rows
    write_json(path, state)
    write_reports(root, day, rows)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', type=date.fromisoformat, default=datetime.now(timezone.utc).date())
    parser.add_argument('--output-dir', type=Path, default=Path('.'))
    parser.add_argument('--config', type=Path, default=Path('config.json'))
    args = parser.parse_args()
    cfg = json.loads(args.config.read_text(encoding='utf-8')) if args.config.exists() else DEFAULT_CONFIG
    try:
        changed = run(args.output_dir, args.date, cfg)
    except (ValueError, KeyError) as exc:
        parser.error(str(exc))
    print('Synthetic simulation updated.' if changed else 'Already processed this date; no simulation changes.')


if __name__ == '__main__':
    main()
