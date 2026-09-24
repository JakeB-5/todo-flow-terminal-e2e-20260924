def safe_divide(numerator, denominator, fallback=None):
    """Return the quotient, or fallback when the denominator equals zero."""
    if denominator == 0:
        return fallback
    return numerator / denominator
