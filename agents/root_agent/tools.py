from datetime import datetime, timezone


def get_current_time() -> dict:
    """Returns the current UTC date and time."""
    now = datetime.now(timezone.utc)
    return {"utc_time": now.isoformat(), "timestamp": now.timestamp()}


def search_web(query: str) -> dict:
    """Search the web for information about a topic.

    Args:
        query: The search query string.

    Returns:
        A dict containing the query and matching results.
    """
    # Stub — replace with a real provider (e.g. Serper, Tavily, Google Search API)
    return {
        "query": query,
        "results": f"[Stub] No search backend configured. Received query: {query!r}",
    }
