# KnowmoreIQ Framework – Reconciliation & Current Status

This document clarifies the relationship between the multiple frameworks present in this repository and defines **what KnowmoreIQ is right now**.

## History – Three Overlapping Frameworks

| Version | Origin | Module Count | Status |
|---------|--------|--------------|--------|
| Original 12‑Dimension Framework | Co‑designed with Copilot (2025‑2026) | 12 | **Legacy / Reference** – conceptual basis |
| 8‑Module Human Relay Framework | `human-edition/` | 8 | **Legacy / Reference** – used in early seed evaluations |
| AI‑Native 12‑Module Framework | `ai-native-edition/` | 12 | **Current / Evolving** – active specification |

## What KnowmoreIQ Is *Right Now*

**A reference framework for evaluating synthetic cognition under structural stress.**  
The repository contains:

- ✅ **Complete specification** of the AI‑native 12 modules (purpose, dimensions, interpretation).  
- ✅ **Reference task library** (`data/task_bank.json`) – a static set of 50+ tasks (Tiers 1–3).  
- ✅ **Scoring specification** – the intended 45‑point multi‑dimensional system (see `docs/SCORING.md`).  
- ✅ **A prototype seed runner** (`seed_runner.py`) – implements a *single* heuristic (Structural Fidelity) for one seed (“Glitch in the Archive”).  
- ❌ **No full generalized evaluation engine** – the 45‑point scoring is not yet implemented in code.  
- ❌ **No automated task bank runner** – tasks are reference only.

Thus: **KnowmoreIQ is fully specified but only partially implemented.**  
It is a **blueprint for a benchmark**, not yet a production test harness.

## Relationship Between the Frameworks

| Feature | Original 12 | Human Relay | AI‑Native (Current) |
|---------|-------------|-------------|----------------------|
| Modules | 12 | 8 | 12 |
| Scoring | 45‑points (5 axes + bonus) | 5 relay dimensions | 45‑points (specified) |
| Implementation | None | Seed‑based qualitative | Prototype runner (Structural Fidelity only) |
| Status | Legacy | Legacy | Current / Evolving |

All three are **conceptually aligned** – they measure reasoning under stress, ambiguity, and structural pressure. The AI‑native version is the active evolution.

## Unfied Scoring Statement

- **Intended scoring** (not yet fully implemented): 45‑point system per module (five 0‑10 axes + 5‑point integration bonus).  
- **Currently implemented prototype** only computes pass/fail over 6 turns for one seed (Structural Fidelity).  
- **Scales**: 0‑10 per dimension, 0‑100 composite (if implemented).  
- **Output** (when fully implemented): 12‑dimensional radar chart, not a single IQ‑style number.

## What This Repository Is *Not*

- Not a plug‑and‑play benchmark suite for arbitrary AI models.  
- Not a fully automated test harness.  
- Not a production‑ready evaluation system.

## Roadmap to a Complete Implementation

1. **Unify scoring** – implement the 45‑point calculation for all 12 modules.  
2. **Generalize task runner** – consume `task_bank.json` and execute tasks across Tiers 1‑3.  
3. **Add support for multiple seeds** – expand beyond “Glitch in the Archive”.  
4. **Produce radar chart output** – automatic visualization.

These are **future goals**, not current features.

## For Contributors

- See `MAPPING.md` for module‑to‑dimension mapping.  
- See `docs/SCORING.md` for scoring specification.  
- See `docs/REPO_STATUS.md` for implementation status of each component.  
- Use `seed_runner.py` as a prototype reference, not as a full evaluation.

---

*Last updated: 2026‑04‑30*
