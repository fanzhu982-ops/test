import unittest

from pipeline.transformer import (
    calculate_total_sales,
    calculate_retention_rate,
)
from pipeline.validator import validate_record


class TestRetailPipeline(unittest.TestCase):

    def test_total_sales(self):
        self.assertEqual(calculate_total_sales([]), 0)

    def test_retention_rate(self):
        self.assertAlmostEqual(
            calculate_retention_rate(3, 2),
            66.6666667,
            places=5
        )

    def test_retention_rate_with_no_records(self):
        self.assertEqual(calculate_retention_rate(0, 0), 0.0)

    def test_missing_branch_id(self):
            transaction = {
                "branch_id": "",
                "transaction_date": "2026-10-17",
                "customer_tier": "Gold",
                "item_count": "3",
                "revenue": "120.50",
            }
    
            cleaned, errors = validate_record(transaction)
    
            self.assertIsNone(cleaned)
            self.assertIn("Missing branch ID", errors)


if __name__ == "__main__":
    unittest.main()


    


