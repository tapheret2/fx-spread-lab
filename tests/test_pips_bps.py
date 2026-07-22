from fx_spread_lab.spread import pips, cost_bps

def test_pips():
    assert abs(pips(0.0001) - 1.0) < 1e-12

def test_cost_bps():
    assert abs(cost_bps(0.0002, 1.0) - 2.0) < 1e-9
