"""Sentinela monitoring service."""

from __future__ import annotations

from typing import Dict


async def process_event(event: Dict) -> Dict:
    """Analyze an event and decide if a wallet should be reanalyzed."""

    gas_used = event.get("gas_used", 0)
    reanalyze = gas_used > 200
    return {"reanalyze": reanalyze}
