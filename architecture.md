# OFFC System Architecture

---

## High-Level Model

OFFC is composed of 4 abstract layers:

1. Data Layer (FX Market Inputs)
2. Computation Layer (Valuation Engine)
3. Stability Layer (ValuGuard)
4. Output Layer (OFFC Index)

---

## System Flow
---

## Component Breakdown

### 1. Oracle Interface

- fetches real-time FX data
- validates inconsistencies
- normalizes cross-market values

### 2. Basket Engine

- computes weighted aggregation
- applies normalization constraints
- ensures sum(weights) = 1

### 3. Stability Layer

- applies volatility dampening
- detects abnormal market events
- adjusts sensitivity dynamically

---

## Design Philosophy

- deterministic computation
- modular architecture
- external data dependency isolation
- statistical smoothing over raw volatility
