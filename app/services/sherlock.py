import os
from typing import List
import httpx

BITQUERY_API_URL = "https://api.bitquery.io"
BITQUERY_API_KEY = os.getenv("BITQUERY_API_KEY")


def build_graph_query(wallet_address: str) -> str:
    return (
        """
    {{
        ethereum {{
            address(addresses: {{is: \"{addr}\"}}) {{
                balances {{
                    currency {{
                        symbol
                    }}
                    value
                }}
            }}
        }}
    }}
    """.format(addr=wallet_address)
    )


def detect_patterns(data: dict) -> List[str]:
    flags = []
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
    headers = {"X-API-KEY": BITQUERY_API_KEY} if BITQUERY_API_KEY else {}
    payload = {"query": build_graph_query(wallet_address)}
    async with httpx.AsyncClient() as client:
        response = await client.post(BITQUERY_API_URL, json=payload, headers=headers)
    data = response.json()
    return detect_patterns(data)
