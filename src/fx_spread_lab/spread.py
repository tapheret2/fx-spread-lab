from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class QuoteMetrics:
    bid: float
    ask: float
    mid: float
    spread: float
    spread_bps: float
    round_trip_cost_per_unit: float
    round_trip_cost_notional: float | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def quote_metrics(bid: float, ask: float, notional: float | None = None) -> QuoteMetrics:
    if bid <= 0 or ask <= 0:
        raise ValueError("bid/ask must be > 0")
    if ask < bid:
        raise ValueError("ask must be >= bid")
    mid = (bid + ask) / 2.0
    spread = ask - bid
    bps = (spread / mid) * 10_000 if mid else 0.0
    # Round trip: buy at ask, sell at bid
    rt = spread
    rt_n = (spread / mid) * notional if notional is not None and mid else None
    return QuoteMetrics(bid, ask, mid, spread, bps, rt, rt_n)


def mid_price(bid: float, ask: float) -> float:
    """Return mid price for a bid/ask pair."""
    if bid <= 0 or ask <= 0 or ask < bid:
        raise ValueError("invalid bid/ask")
    return (bid + ask) / 2.0


def spread_bps(bid: float, ask: float) -> float:
    """Bid-ask spread in basis points of mid."""
    mid = (bid + ask) / 2.0
    if mid <= 0 or ask < bid:
        raise ValueError("invalid bid/ask")
    return (ask - bid) / mid * 10000.0


def half_spread(bid: float, ask: float) -> float:
    """One-way cost ≈ half the full bid-ask spread."""
    if bid <= 0 or ask <= 0 or ask < bid:
        raise ValueError("invalid bid/ask")
    return (ask - bid) / 2.0


def effective_mid_slippage(bid: float, ask: float, side: str = "buy") -> float:
    """Signed slip from mid: + for buy (pay ask), - for sell (hit bid)."""
    m = mid_price(bid, ask)
    side = side.lower()
    if side == "buy":
        return ask - m
    if side == "sell":
        return bid - m
    raise ValueError("side must be buy or sell")

def pips(diff: float, pip_size: float = 0.0001) -> float:
    """Convert a price difference into pips."""
    if pip_size <= 0:
        raise ValueError("pip_size must be > 0")
    return float(diff) / float(pip_size)


def cost_bps(spread: float, mid: float) -> float:
    """Round-trip spread cost in basis points of mid."""
    if mid <= 0:
        raise ValueError("mid must be > 0")
    return 10000.0 * float(spread) / float(mid)
