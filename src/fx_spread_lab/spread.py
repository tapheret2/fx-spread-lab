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
