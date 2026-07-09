from __future__ import annotations

import argparse
import json
import sys

from .spread import quote_metrics


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="fx-spread-lab")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cost")
    c.add_argument("--bid", type=float, required=True)
    c.add_argument("--ask", type=float, required=True)
    c.add_argument("--notional", type=float, default=None)
    args = p.parse_args(argv)
    if args.cmd == "cost":
        m = quote_metrics(args.bid, args.ask, args.notional)
        print(json.dumps(m.to_dict(), indent=2))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
