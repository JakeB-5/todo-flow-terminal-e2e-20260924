def compact(text):
    """Collapse whitespace runs to ASCII spaces and trim the edges."""
    return " ".join(text.split())
