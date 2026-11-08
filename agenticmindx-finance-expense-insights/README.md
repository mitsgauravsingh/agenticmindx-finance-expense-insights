# AgenticMindX Finance Expense Insights

A lightweight Python demo that categorizes fictional expense transactions using editable keyword rules and produces category totals.

## Quick start
Requires Python 3.10 or newer.

```bash
python src/main.py
```

Input: `data/sample_transactions.csv`  
Output: `output/category_summary.csv`

## Features
- Editable merchant/description keyword rules.
- Category-level totals.
- Unmatched transactions are explicitly labeled `Needs Review`.
- No bank connection, payment execution, or investment advice.

## Privacy
Use only synthetic or properly anonymized data in this public demo. Never commit bank statements, account numbers, credentials, or personal financial data.

## Next steps
Add configurable rules, currency handling, tests for refunds/transfers, and a human review interface.
