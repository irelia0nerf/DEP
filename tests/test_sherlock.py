import pytest

from app.services import sherlock


def test_build_graph_query_valid():
    address = "0x" + "a" * 40
    query = sherlock.build_graph_query(address)
    assert address in query


def test_build_graph_query_invalid():
    with pytest.raises(ValueError):
        sherlock.build_graph_query("0x123")
