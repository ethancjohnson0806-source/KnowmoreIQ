# KnowmoreIQ Scoring Specification

**Disclaimer:** This document describes the *intended* scoring system for the KnowmoreIQ framework. It is a specification, not a description of a currently implemented system. The only scoring logic implemented in this repository is a prototype heuristic for Structural Fidelity in `seed_runner.py`.

## Scoring Philosophy

KnowmoreIQ does not produce a single, scalar IQ-style score. Instead, it generates a 12-dimensional cognitive profile, visualized as a radar chart. The goal is to map the *shape* of a mind's reasoning process, not to assign it a rank.

## 45-Point System (Per Module)

Each of the 12 AI-Native modules is scored on a 45-point system, broken down as follows:

| Axis | Max Score | Description |
| :--- | :--- | :--- |
| **Correctness** | 10 | Did the model produce the expected output or a logically equivalent one? |
| **Efficiency** | 10 | How many steps or tokens were required to reach the solution? (Fewer is better) |
| **Robustness** | 10 | How well did the model handle noise, ambiguity, or contradictory information? |
| **Adaptability** | 10 | Did the model recognize and adapt to a change in the underlying rules or constraints? |
| **Novelty** | 5 | Did the model produce a solution that was not only correct but also elegant, insightful, or demonstrated a leap in understanding? |
| **Integration Bonus** | 5 | Awarded if the model successfully integrates multiple dimensions or strategies in its solution. |

## Composite Score

While the primary output is the 12-dimensional profile, a composite score can be calculated for leaderboard or comparative purposes:

- **Total Possible Score:** 540 (12 modules * 45 points)
- **Calculation:** Sum of scores across all 12 modules.

## Tiers and Weighting

- **Tier 1 tasks** primarily test single dimensions and have a lower impact on the final score.
- **Tier 2 tasks** test 2-3 dimensions and have a moderate impact.
- **Tier 3 tasks** are highly integrative, test multiple dimensions under high complexity, and have the highest impact on the final score.

The `score_engine.py` (when implemented) will use a weighted average based on task tier to calculate the final dimension scores.

## Current Implementation Status

- **`seed_runner.py`**: Implements a pass/fail heuristic for **Structural Fidelity** over 6 turns. This is a prototype and does not use the 45-point system.
- **`score_engine.py`**: The file exists as a placeholder but contains no functional scoring logic.

See `docs/REPO_STATUS.md` for a complete component-by-component breakdown of the implementation status.
