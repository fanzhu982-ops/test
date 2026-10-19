from datetime import date

def validate_record(raw_record):
    """Validate one raw transaction record."""
    errors = []
    cleaned = {}

    # Check branch ID
    branch_id = str(raw_record.get("branch_id", "")).strip()

    if not branch_id:
        errors.append("Missing branch ID")
    else:
        cleaned["branch_id"] = branch_id

    # Check transaction date
    try:
        transaction_date = date.fromisoformat(
            str(raw_record.get("transaction_date", "")).strip()
        )
        cleaned["transaction_date"] = transaction_date
    except (ValueError, TypeError):
        errors.append("Invalid transaction date")

    # Check customer tier
    customer_tier = str(
        raw_record.get("customer_tier", "")
    ).strip()

    if not customer_tier:
        errors.append("Missing customer tier")
    else:
        cleaned["customer_tier"] = customer_tier

    # Check item count
    try:
        item_count = int(raw_record.get("item_count"))

        if item_count < 0:
            errors.append("Negative item count")
        else:
            cleaned["item_count"] = item_count
    except (ValueError, TypeError):
        errors.append("Invalid item count")

    # Check revenue
    try:
        revenue = float(raw_record.get("revenue"))

        if revenue < 0:
            errors.append("Negative revenue")
        else:
            cleaned["revenue"] = revenue
    except (ValueError, TypeError):
        errors.append("Invalid revenue")

    if errors:
        return None, errors

    return cleaned, []



