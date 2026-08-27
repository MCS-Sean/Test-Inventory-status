# Synthetic Inventory Checker

A transparent portfolio simulation of inventory classification, lead-time risk,
and replenishment planning. **Every product, quantity, history record, and lead
time is fictional. There are no costs, prices, sales values, real SKU mappings,
or company exports.** No real orders are placed and no external service is called.

## Start locally

Requires Python 3.11 or newer. Uses only the standard library; no installation of
third-party packages, API keys, or paid services required.

```sh
python -m unittest -v
python inventory_checker.py
```

Open `reports/latest.md` for the inventory report and `reports/latest.json` for
machine-readable details. `data/state.json` holds the synthetic inventory,
rolling history, and outstanding simulated orders. All output dates use UTC
calendar days, not business days.

The download includes a generated sample as of 2026-08-27. Repeating that date
produces identical bytes and does not create another simulated order. Future
runs process each missed day in order but only save the latest report. They do
not create backdated Git commits. Running backward is rejected.

To experiment without altering the included state:

```sh
python inventory_checker.py --date 2026-08-27 --output-dir experiment
python inventory_checker.py --date 2026-09-10 --output-dir experiment
```

## Movement classification

These are the user's report labels, with a deliberately nonfinancial ranking:

| Class | Synthetic classification |
|---|---|
| A - Top Movers | Highest 25 core items by units sold in the preceding 12 calendar months |
| B - Core Products | Next 75 core items by the same ranking |
| C - Slow Moving | Remaining core items with sales in that period |
| Dead Inv | No sales in the preceding 12 calendar months |

All 160 generated items are marked core. The classifier also supports a
`Non-core` result for active non-core items, excluded from automatic ordering.
Zero-sales items are labeled Dead Inv even when stock is zero; their health then
reads `Inactive / no stock` rather than implying there is dead stock on hand.
SKU breaks sales-volume ties deterministically. Classes are recalculated daily.

**Matching limits:** the original report's B group was the next 75 items. Its A
cutoff was not confirmed; 25 is an editable demonstration default, not a claimed
match. The original ranking included annual sales value; this project substitutes
units sold and does not reproduce that financial ranking. Its surplus/push rules
and exact thresholds are not reproduced. Labels are movement ranks, not a
value-based ABC/Pareto analysis. Edit `a_count` and `b_count` in `config.json`.

## Lead times versus stocking

Synthetic supplier means range from 7 to 90 calendar days. Actual simulated
receipt times vary around each item's mean. The generator uses steady, seasonal,
intermittent, and inactive demand; those behaviors are separate from movement
classes. The mix and initial stock multipliers are illustrative, not measured
from company records.

Let:

- d = mean daily requested demand over the latest 90 days, including zero days;
- s = population standard deviation of that daily demand;
- L and sL = configured supplier lead-time mean and standard deviation;
- R = review interval (1 day by default), T = class order-cycle buffer;
- z = class safety factor.

The planning calculations are:

```text
Safety stock = ceil(z * sqrt((L + R) * s² + d² * sL²))
Reorder point = ceil(d * (L + R) + safety stock)
Target stock = ceil(d * (L + R + T) + safety stock)
Inventory position = on hand + outstanding incoming quantities
Suggested quantity = target stock - inventory position, if position <= reorder point
```

Suggested quantities are nonnegative, respect minimum order quantities, and
round up to whole packs. Defaults: A uses z=2.05 and T=14; B uses 1.65 and 21;
C uses 1.28 and 30. These are adjustable demo policies, not optimized service
levels or promised fill rates. Longer/less reliable supply generally increases
stocking needs. For constant demand of 10/day, lead time 7 days, lead SD 1 day,
and class A, safety stock is 21, reorder point 101, and target stock 241.

Outstanding orders prevent duplicate purchases. A separate date-by-date balance
projection includes only receipts available on each day and checks for shortages
through ceil(L + z*sL). This can flag `Lead-time risk` even when total on-order
quantity looks sufficient. Coverage days = on hand / d; coverage ratio =
coverage days / L. No-demand coverage is null/N/A, never infinity.

Every day: receive due orders, generate demand, fulfill available stock, record
lost sales, classify, analyze, and place **simulated** replenishment orders.
Report stock/on-order values are **before new orders**; `simulated_order_placed`
and `new_order_due` show the new supply separately. State contains the new orders.

## Health and limitations

Stock health is independent of movement class: Dead inventory, Inactive / no
stock, Non-core review, Dormant demand, Stockout, Lead-time risk, Reorder, Excess,
or Healthy. Higher urgency takes precedence. Excess health requires on-hand
stock above 1.5 times target; `excess_above_target` shows units above target even
below that alert threshold. Dead/non-core/no-recent-demand items do not reorder
automatically and require manual review.

Demand is observed even when stock is unavailable, preventing stockouts from
artificially suppressing the forecast. Movement ranking still uses fulfilled
sales as a turn report would, so a prolonged stockout can reduce movement rank.
Demand is lost rather than backordered. There are no reservations or allocations.
The initial 366-day history assumes unlimited synthetic fulfillment; actual stock
conservation starts on the first simulation day. History is retained for 366 days.

The safety-stock approximation assumes independent, stationary demand and lead
times. It is deliberately a baseline; seasonal/intermittent demand violates those
assumptions. A rolling mean is not a full seasonal or intermittent forecasting
model. Scheduled receipt dates are known in the simulation; the risk projection
is not a probability guarantee. Critical spares, capacity, business calendars,
cost optimization, transfers, and real ERP purchasing are outside scope.

Change policies in `config.json` and start a fresh output directory. Changing
config against existing state is rejected to prevent silently mixing scenarios.
Do not import a real export: this project is not an anonymization tool. Even
renamed real SKUs or scaled real quantities can disclose business patterns.

## Enable daily GitHub execution

1. Create your own standalone repository, then extract this ZIP and add the
   **contents** of this folder at the repository root, including `.github`.
   Commit the source, config, data, reports, and workflow to the default branch.
2. Ensure Actions is enabled and repository policy allows the workflow's
   `contents: write` permission. The workflow pushes normally; it cannot bypass
   branch protections. A protected branch should use your approved PR workflow
   instead of weakening protections for this demo.
3. Optionally configure **Settings > Secrets and variables > Actions > Variables**:
   - `INVENTORY_AUTHOR_NAME`: your own Git author name.
   - `INVENTORY_AUTHOR_EMAIL`: your own GitHub-linked email, preferably the exact
     GitHub-provided noreply address from your account's email settings.
   Set both or neither. Values are passed through environment variables, not
   interpolated into shell code. Never use another person's identity.
4. Open Actions, select **Daily synthetic inventory**, and choose **Run workflow**
   on the default branch. Check the job log and the updated report.

The supplied schedule is 14:23 UTC daily. GitHub schedules may be delayed or
skipped; this is not an exact-time SLA. Public scheduled workflows can be disabled
by GitHub after 60 days without repository activity. The workflow serializes
runs and only commits the three explicit generated files when their bytes change.
Concurrent manual pushes can cause a normal non-fast-forward failure; rerun the
workflow to retry against the latest branch, never force-push.

Without author variables, commits use `github-actions[bot]` and will not become
your personal contributions. Your own linked author identity can make eligible
commits attributable to you; GitHub's repository and branch contribution rules
still apply. All commit messages identify the output as automated simulation.
This is a portfolio automation demonstration, not evidence of daily manual work
or a guarantee of daily green squares. GitHub setup has **not** been performed
for you: this package only provides the ready-to-install workflow.

References:

- [GitHub scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [GitHub workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub contribution rules](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference)
