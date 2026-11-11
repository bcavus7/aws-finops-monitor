def analyze_budget(limit, spent, threshold=80):
    if limit <= 0:
        raise ValueError("Budget must be greater than zero")

    remaining = limit - spent
    percentage = (spent / limit) * 100
    warning = percentage >= threshold

    return remaining, percentage, warning
