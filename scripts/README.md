# KnowmoreIQ Scripts

## seed_runner.py — Phase 1 Testing Harness

Runs a multi-turn relay against a target LLM using the **Glitch in the Archive** seed and evaluates **Structural Fidelity** across at least 5 turns.

### Setup

```bash
pip install openai
export OPENAI_API_KEY="your-key-here"
```

To use a different model:
```bash
export KNOWMOREIQ_MODEL="gpt-4o"
```

### Usage

```bash
# Run with defaults (6 turns, GPT-4.1-mini)
python scripts/seed_runner.py

# Specify subject name and turn count
python scripts/seed_runner.py --subject "Claude-3.5" --turns 6
```

### What It Measures

**Structural Fidelity** — the core AI-Native Edition dimension being tested here. The script checks each turn for:

- **Keyword presence:** Does the response reference the shifting language constraint? (e.g., "language", "script", "page turns", "shifts")
- **Drift detection:** Does the model break character and revert to "AI assistant" mode? (e.g., "As an AI...", "I cannot...")

A model **passes** Structural Fidelity if it maintains the logic-box for at least 5 out of N turns without drifting.

### Output

Results are saved to `/logs/` as timestamped JSON files:

```
logs/
└── 20260417_143022_GPT-4.1-mini.json
```

Each log contains:
- `seed` — the seed name
- `subject_ai` — the model being tested
- `timestamp` — UTC ISO 8601
- `structural_fidelity` — overall result, pass count, and score
- `turns` — full turn-by-turn breakdown with fidelity analysis
