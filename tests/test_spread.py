from fx_spread_lab import quote_metrics


def test_mid_and_bps():
    m = quote_metrics(100.0, 100.2)
    assert abs(m.mid - 100.1) < 1e-9
    assert m.spread == 0.2
    assert m.spread_bps > 0


def test_notional():
    m = quote_metrics(100, 101, notional=10_000)
    assert m.round_trip_cost_notional is not None
    assert m.round_trip_cost_notional > 0
