
from pipeline.schema import TransactionRecord, RetailAnalytics
from pipeline.validator import validate_record
from pipeline.transformer import (
    calculate_total_sales,
    filter_active_transactions,
    calculate_retention_rate,
    find_top_branch,
    calculate_tier_sales,
    calculate_net_revenues,
)
from pipeline.reporter import print_report


def main():
    """Run the retail analytics pipeline."""

    # Sample raw transaction records
    raw_transactions = [
        {
            "branch_id": "B001",
            "transaction_date": "2026-10-17",
            "customer_tier": "Gold",
            "item_count": "3",
            "revenue": "120.50",
        },
        {
            "branch_id": "B002",
            "transaction_date": "2026-10-17",
            "customer_tier": "Silver",
            "item_count": "2",
            "revenue": "75.00",
        },
        {
            "branch_id": "",
            "transaction_date": "2026-10-17",
            "customer_tier": "Gold",
            "item_count": "1",
            "revenue": "40.00",
        },
    ]

    valid_transactions = []
    errors_found = []

    # Validate each record and create transaction objects
    for raw_record in raw_transactions:
        cleaned, errors = validate_record(raw_record)

        if errors:
            errors_found.append(errors)
            continue

        transaction = TransactionRecord(
            cleaned["branch_id"],
            cleaned["transaction_date"],
            cleaned["customer_tier"],
            cleaned["item_count"],
            cleaned["revenue"],
        )

        valid_transactions.append(transaction)

    # Filter active transactions
    active_transactions = filter_active_transactions(
        valid_transactions
    )

    # Illustrative tax rates, not supplied by the assignment
    tax_rates = {
        "B001": 0.13,
        "B002": 0.15,
    }

    net_revenues = calculate_net_revenues(
        active_transactions,
        tax_rates,
    )

    print("Net revenue after regional tax:", net_revenues)

    # Use the RetailAnalytics class to calculate total sales
    analytics = RetailAnalytics(active_transactions)
    total_sales = analytics.get_total_sales()

    # Calculate business metrics
    retention_rate = calculate_retention_rate(
        len(raw_transactions),
        len(valid_transactions),
    )

    top_branch = find_top_branch(active_transactions)
    tier_sales = calculate_tier_sales(active_transactions)

    # Display the report
    print_report(
        valid_transactions,
        active_transactions,
        errors_found,
        total_sales,
        retention_rate,
        top_branch,
        tier_sales,
    )


if __name__ == "__main__":
    main()
