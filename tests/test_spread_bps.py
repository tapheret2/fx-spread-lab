from fx_spread_lab.spread import spread_bps

def test_spread_bps():
    # bid 100 ask 101 mid 100.5 → 1/100.5 * 10000
    bps = spread_bps(100, 101)
    assert abs(bps - (1 / 100.5 * 10000)) < 1e-6
