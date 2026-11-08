"""Rule-based expense categorization for demonstration data."""
import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

RULES = {
    "Groceries": ("grocery", "market", "supermarket"),
    "Software": ("cloud", "hosting", "software", "subscription"),
    "Transport": ("taxi", "ride", "train", "bus"),
}


def categorize(description: str) -> str:
    normalized = description.casefold()
    for category, keywords in RULES.items():
        if any(keyword in normalized for keyword in keywords):
            return category
    return "Needs Review"


def summarize(source: str, destination: str) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = defaultdict(Decimal)
    with open(source, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            amount = Decimal(row["amount"])
            totals[categorize(row["description"])] += amount

    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "total_amount"])
        for category in sorted(totals):
            writer.writerow([category, f"{totals[category]:.2f}"])
    return dict(totals)
