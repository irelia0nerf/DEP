import os
import sys

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
async def test_snapshot_event():
    event = {"foo": "bar"}
    snapshot = await mirror_engine.snapshot_event(event)
    assert snapshot["event"] == event
    assert "timestamp" in snapshot
