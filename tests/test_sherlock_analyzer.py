import pytest

from src.sherlock import analyzer


def test_build_graph_query_valid():
    addr = "0x" + "a" * 40
    query, variables = analyzer.build_graph_query(addr)
    assert "$addr" in query
    assert variables["addr"] == addr


def test_build_graph_query_invalid():
    with pytest.raises(ValueError):
        analyzer.build_graph_query("0x123")
