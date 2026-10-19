def print_report(
    valid_transactions,
    active_transactions,
    errors_found,
    total_sales,
    retention_rate,
    top_branch,
    tier_sales
):
    """Display a summary report of retail analytics."""

    print("\n===== RETAIL ANALYTICS REPORT =====")
    print(f"Valid transactions: {len(valid_transactions)}")
    print(f"Active transactions: {len(active_transactions)}")
    print(f"Errors found: {errors_found}")
    print(f"Total gross sales: {total_sales}")
    print(f"Retention rate: {retention_rate:.2f}%")
    print(f"Top-performing branch: {top_branch}")
    print(f"Sales by customer tier: {tier_sales}")
    print("==================================")

