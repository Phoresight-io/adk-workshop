from __future__ import annotations

_grants: dict[str, dict] = {}


def add_grant(
    name: str,
    funder: str,
    amount: str,
    deadline: str,
    status: str,
    eligibility_tags: list[str],
    notes: str = "",
) -> dict:
    """Add a new grant opportunity to the tracker.

    Args:
        name: Unique grant or program title.
        funder: Organization or agency offering the grant.
        amount: Award amount as a string (e.g. "$50,000" or "up to $100k").
        deadline: Application deadline in YYYY-MM-DD format.
        status: Current stage — one of: researching, drafting, submitted, awarded, rejected.
        eligibility_tags: Eligibility categories (e.g. ["women-led", "BIPOC", "veteran-owned"]).
        notes: Optional opening note.

    Returns:
        The newly created grant record, or an error dict if the name already exists.
    """
    if name in _grants:
        return {"error": f"Grant '{name}' already exists. Use update_status or add_note to modify it."}
    record: dict = {
        "name": name,
        "funder": funder,
        "amount": amount,
        "deadline": deadline,
        "status": status,
        "eligibility_tags": eligibility_tags,
        "notes": [notes] if notes else [],
    }
    _grants[name] = record
    return record


def update_status(name: str, status: str) -> dict:
    """Update the application status of an existing grant.

    Args:
        name: The grant title to update.
        status: New status — one of: researching, drafting, submitted, awarded, rejected.

    Returns:
        The updated grant record, or an error dict if not found.
    """
    if name not in _grants:
        return {"error": f"Grant '{name}' not found."}
    _grants[name]["status"] = status
    return _grants[name]


def get_deadlines() -> list[dict]:
    """Return all tracked grants sorted by deadline, soonest first.

    Returns:
        List of grant records ordered by deadline date string (YYYY-MM-DD).
    """
    return sorted(_grants.values(), key=lambda g: g["deadline"])


def get_pipeline() -> dict[str, list[dict]]:
    """Return the full grant pipeline grouped by status.

    Returns:
        Dict mapping each status to the list of grants in that stage.
    """
    pipeline: dict[str, list[dict]] = {}
    for grant in _grants.values():
        pipeline.setdefault(grant["status"], []).append(grant)
    return pipeline


def add_note(name: str, note: str) -> dict:
    """Append a note to an existing grant record.

    Args:
        name: The grant title to annotate.
        note: The note text to append.

    Returns:
        The updated grant record, or an error dict if not found.
    """
    if name not in _grants:
        return {"error": f"Grant '{name}' not found."}
    _grants[name]["notes"].append(note)
    return _grants[name]
