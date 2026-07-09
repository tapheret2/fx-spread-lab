# fx-spread-lab

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Compute **mid**, **spread bps**, and **round-trip cost** from bid/ask quotes. Educational microstructure mini-lab.

## CLI

```bash
pip install -e ".[dev]"
fx-spread-lab cost --bid 1.0850 --ask 1.0852
fx-spread-lab cost --bid 65000 --ask 65050 --notional 10000
```
