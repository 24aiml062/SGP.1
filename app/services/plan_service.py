from __future__ import annotations

# Simple in-memory plan store (single-user / demo).
# Replace with a DB-backed store when multi-user auth is added.
_plan: dict = {}


def get_plan() -> dict:
    """Return the current growth plan (empty dict if not set)."""
    return dict(_plan)


def save_plan(data: dict) -> dict:
    """Persist the growth plan and return it."""
    _plan.clear()
    _plan.update(data)
    return dict(_plan)
