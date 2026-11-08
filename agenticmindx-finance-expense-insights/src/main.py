from expense_insights import summarize


if __name__ == "__main__":
    totals = summarize("data/sample_transactions.csv", "output/category_summary.csv")
    for category, amount in sorted(totals.items()):
        print(f"{category}: {amount:.2f}")
    print("Wrote output/category_summary.csv")
