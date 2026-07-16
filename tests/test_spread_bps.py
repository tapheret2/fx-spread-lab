from fx_spread_lab.spread import spread_bps

def test_spread_bps_positive():
    assert spread_bps(100, 100.1) > 0
