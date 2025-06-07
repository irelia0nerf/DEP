from app.services import gas_monitor


def test_detect_gas_patterns_high_avg():
    flags, avg = gas_monitor.detect_gas_patterns([400000, 450000])
    assert "HIGH_AVG_GAS" in flags
    assert avg > 300000


def test_detect_gas_patterns_spike_and_extreme():
    flags, _ = gas_monitor.detect_gas_patterns([100000, 700000])
    assert "GAS_SPIKE" in flags
    assert "EXTREME_GAS_USAGE" in flags


def test_detect_gas_patterns_normal_usage():
    flags, avg = gas_monitor.detect_gas_patterns([21000, 22000, 23000])
    assert flags == []
    assert 21000 <= avg <= 23000
