from __future__ import annotations

import os
import re
from typing import List, Tuple

import httpx

BITQUERY_API_URL = "https://api.bitquery.io"
BITQUERY_API_KEY = os.getenv("BITQUERY_API_KEY")

ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")


def build_graph_query(wallet_address: str) -> Tuple[str, dict]:
    if not ADDRESS_RE.match(wallet_address):
        raise ValueError("Invalid wallet address")

    query = """
    query($addr: String!) {
        ethereum {
            address(addresses: {is: $addr}) {
                balances {
                    currency {
                        symbol
                    }
                    value
                }
            }
        }
    }
    """
    return query, {"addr": wallet_address}


def detect_patterns(data: dict) -> List[str]:
    flags: List[str] = []
    balances = (
        data.get("data", {})
        .get("ethereum", {})
        .get("address", [{}])[0]
        .get("balances", [])
    )
    for bal in balances:
        if bal.get("value", 0) and bal["value"] > 10000:
            flags.append("HIGH_BALANCE")
    return flags


async def analyze_wallet(wallet_address: str) -> List[str]:
    """Analyze on-chain data and return reputation flags."""

    headers = {"X-API-KEY": BITQUERY_API_KEY} if BITQUERY_API_KEY else {}
    query, variables = build_graph_query(wallet_address)
    payload = {"query": query, "variables": variables}
    async with httpx.AsyncClient() as client:
        response = await client.post(BITQUERY_API_URL, json=payload, headers=headers)
    data = response.json()
    return detect_patterns(data)
