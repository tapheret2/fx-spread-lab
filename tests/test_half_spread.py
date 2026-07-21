from fx_spread_lab.spread import effective_mid_slippage, half_spread

def test_half_spread():
    assert abs(half_spread(1.10, 1.12) - 0.01) < 1e-12

def test_buy_slip_positive():
    assert effective_mid_slippage(100, 102, "buy") > 0
    assert effective_mid_slippage(100, 102, "sell") < 0
