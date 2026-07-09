from fx_spread_lab.spread import mid_price

def test_mid_price():
    assert abs(mid_price(100, 102) - 101) < 1e-9
