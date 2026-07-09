# fx-spread-lab

Compute **mid**, **spread bps**, and **round-trip cost** from bid/ask quotes. Educational microstructure mini-lab.

## CLI

```bash
pip install -e ".[dev]"
fx-spread-lab cost --bid 1.0850 --ask 1.0852
fx-spread-lab cost --bid 65000 --ask 65050 --notional 10000
```
