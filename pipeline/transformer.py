
def calculate_net_revenue(revenue, tax_rate):
    """Calculate revenue after deducting tax."""
    return revenue * (1 - tax_rate)


def calculate_net_revenues(transactions, tax_rates):
    """Calculate net revenue for each transaction using its region's tax rate."""
    return [
        calculate_net_revenue(
            transaction.revenue,
            tax_rates.get(transaction.branch_id, 0)
        )
        for transaction in transactions
    ]


def get_transaction_dates(transactions):
    """Use map to extract transaction dates."""
    return list(map(lambda transaction: transaction.transaction_date, transactions))

def filter_active_transactions(transactions):
    """Keep transactions with positive revenue."""
    return list(
        filter(lambda transaction: transaction.revenue > 0, transactions)
    )


def calculate_total_sales(transactions):
    """Calculate total gross sales from transactions."""
    return sum(
        transaction.revenue for transaction in transactions
    )


def calculate_retention_rate(raw_count, valid_count):
    """Calculate the percentage of records that passed validation."""
    if raw_count == 0:
        return 0.0

    return (valid_count / raw_count) * 100

def find_top_branch(transactions):
    """Return the branch ID with the highest total sales."""
    sales_by_branch = {}

    for transaction in transactions:
        branch_id = transaction.branch_id
        revenue = transaction.revenue

        sales_by_branch[branch_id] = (
            sales_by_branch.get(branch_id, 0) + revenue
        )

    if not sales_by_branch:
        return None

    return max(sales_by_branch, key=sales_by_branch.get)

def calculate_tier_sales(transactions):
    """Calculate total revenue for each customer tier."""
    sales_by_tier = {}

    for transaction in transactions:
        tier = transaction.customer_tier
        revenue = transaction.revenue

        sales_by_tier[tier] = (
            sales_by_tier.get(tier, 0) + revenue
        )

    return sales_by_tier
