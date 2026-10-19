class TransactionRecord:
    """Represent one retail transaction."""

    def __init__(
        self,
        branch_id,
        transaction_date,
        customer_tier,
        item_count,
        revenue
    ):
        self.branch_id = branch_id
        self.transaction_date = transaction_date
        self.customer_tier = customer_tier
        self.item_count = item_count
        self.revenue = revenue


class RetailAnalytics:
    """Analyze a collection of retail transactions."""

    def __init__(self, transactions):
        self.transactions = transactions

    def get_total_sales(self):
        """Calculate total revenue from the transactions."""
        return sum(
            transaction.revenue
            for transaction in self.transactions
        )
