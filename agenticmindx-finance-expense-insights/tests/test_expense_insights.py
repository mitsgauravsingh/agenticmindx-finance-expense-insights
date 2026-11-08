import unittest
from src.expense_insights import categorize


class CategorizationTests(unittest.TestCase):
    def test_known_category(self):
        self.assertEqual(categorize("Monthly cloud hosting"), "Software")

    def test_unknown_is_reviewed(self):
        self.assertEqual(categorize("Unlisted vendor"), "Needs Review")


if __name__ == "__main__":
    unittest.main()
