import os
import sys
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from app.services import mirror_engine  # noqa: E402


class FakeCollection:
    def __init__(self):
        self.docs = []

    async def insert_one(self, doc):
        self.docs.append(doc)

    def find(self, query):
        matching = [
            d
            for d in self.docs
            if all(d.get(k) == v for k, v in query.items())
        ]

        class Cursor:
            def __init__(self, docs):
                self.docs = docs

            def sort(self, key, direction):
                self.docs.sort(key=lambda x: x.get(key), reverse=direction == -1)
                return self

            async def to_list(self, length=None):
                if length is None:
                    return self.docs
                return self.docs[:length]

        return Cursor(matching)


class FakeDB:
    def __init__(self):
        self.snapshots = FakeCollection()
        self.analysis = FakeCollection()


def override_db():
    return FakeDB()


@pytest.mark.asyncio
async def test_snapshot_and_compare(monkeypatch):
    db = FakeDB()
    monkeypatch.setattr(mirror_engine, "get_db", lambda: db)

    first = {"wallet": "0x1", "flags": ["A"], "score": 10}
    second = {"wallet": "0x1", "flags": ["A", "B"], "score": 20}

    await mirror_engine.snapshot_event(first)
    await mirror_engine.snapshot_event(second)

    diff = await mirror_engine.compare_snapshots("0x1")
    assert diff["score_change"] == 10
    assert diff["flags_added"] == ["B"]
    assert diff["flags_removed"] == []
