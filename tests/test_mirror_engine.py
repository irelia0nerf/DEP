from datetime import datetime

import pytest

from app.services import mirror_engine


class DummyCollection:
    def __init__(self):
        self.items = []

    async def insert_one(self, doc):
        self.items.append(doc)

    async def find_one(self, query, sort=None):
        wallet = query.get("wallet")
        docs = [d for d in self.items if d.get("wallet") == wallet]
        if not docs:
            return None
        if sort:
            key, order = sort[0]
            docs.sort(key=lambda d: d[key], reverse=order == -1)
        return docs[0]


class DummyDB:
    def __init__(self):
        self.snapshots = DummyCollection()


@pytest.mark.asyncio
async def test_save_snapshot():
    db = DummyDB()
    snap = {"wallet": "0xabc", "score": 1, "flags": [], "timestamp": datetime.utcnow()}
    await mirror_engine.save_snapshot(snap, db)
    assert db.snapshots.items[0]["wallet"] == "0xabc"


@pytest.mark.asyncio
async def test_compare_snapshot_diff():
    db = DummyDB()
    first = {
        "wallet": "0xabc",
        "score": 10,
        "flags": ["A"],
        "timestamp": datetime(2024, 1, 1),
    }
    await mirror_engine.save_snapshot(first, db)
    second = {
        "wallet": "0xabc",
        "score": 15,
        "flags": ["A", "B"],
        "timestamp": datetime(2024, 1, 2),
    }
    diff = await mirror_engine.compare_snapshot("0xabc", second, db)
    assert diff["score_change"] == 5
    assert diff["added_flags"] == ["B"]
    assert diff["removed_flags"] == []
