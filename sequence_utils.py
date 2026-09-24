"""Utilities for preserving sequence order."""


def ordered_unique(values):
    """Return distinct hashable values in first-occurrence order."""
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
