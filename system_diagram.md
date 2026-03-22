# OFFC System Diagram

## Flow Architecture

FX MARKETS
   ↓
ORACLE DATA FEED
   ↓
BASKET ENGINE (WEIGHTED MODEL)
   ↓
VALUATION ENGINE
   ↓
VALU GUARD STABILITY FILTER
   ↓
OFFC INDEX OUTPUT

---

## Conceptual Model

- Input: global currency fluctuations
- Process: weighted aggregation + stability filtering
- Output: composite digital value index
