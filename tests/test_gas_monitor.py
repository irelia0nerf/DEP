from app.services import gas_monitor


def test_gas_spike_flag():
    result = gas_monitor.analyze_gas_usage([10, 20, 100])
    assert "GAS_SPIKE" in result["flags"]


def test_low_gas_flag():
    result = gas_monitor.analyze_gas_usage([5, 6, 8])
    assert "LOW_GAS_USAGE" in result["flags"]
