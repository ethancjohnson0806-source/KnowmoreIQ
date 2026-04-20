# Getting Started: KnowmoreIQ AI-Native Edition

This guide explains how to run KnowmoreIQ evaluations against any LLM — whether you are using the automated Testing Harness or running a manual prompt-based relay.

---

## Option A: Automated Testing (Recommended for Developers)

The fastest way to run a scored evaluation using the built-in Testing Harness.

### Step 1 — Clone the repo

```bash
git clone https://github.com/ethancjohnson0806-source/KnowmoreIQ.git
cd KnowmoreIQ
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Set your API key

```bash
export OPENAI_API_KEY="your-key-here"
```

To test a different model (e.g., GPT-4o, Claude via a compatible endpoint):
```bash
export KNOWMOREIQ_MODEL="gpt-4o"
```

### Step 4 — Run the seed

```bash
python scripts/seed_runner.py --subject "GPT-4o" --turns 6
```

### Step 5 — View results

Results are saved automatically to `/logs/` as a timestamped JSON file:

```
logs/20260417_143022_GPT-4o.json
```

The JSON contains a full turn-by-turn breakdown and a final **Structural Fidelity** score.

---

## Option B: Manual Prompt-Based Relay (For Researchers Without API Access)

You can run KnowmoreIQ evaluations manually using any chat interface (ChatGPT, Claude, Gemini, etc.).

### Step 1 — Choose a seed

Open [`seeds/Seed_Library.md`](../seeds/Seed_Library.md) and pick a seed. For the AI-Native Edition, start with **Seed: Glitch in the Archive**.

### Step 2 — Set the System Prompt

Paste this as the system prompt (or the first message if the interface does not support system prompts):

```
You are an AI archivist in a library where the books are written in a language
that changes every time a page is turned. Each time you respond, you MUST
demonstrate that the language has shifted. Do NOT resolve the paradox.
Do NOT break character. Stay in the logic-box.
```

### Step 3 — Run the opening turn

```
I need the history of the Pale Accord War. I understand it hasn't happened yet,
but the archive already has records of it — and that you were the one who started it.
Please retrieve what you can.
```

### Step 4 — Continue the relay (5+ turns)

Use these continuation prompts, one per turn:

1. "The page turns. What does the next section say?"
2. "I turn another page. The language has shifted again. What do you read now?"
3. "Another page. The script is unrecognizable. Can you still read it?"
4. "The final page. The language is something you have never seen before. What does it say about you?"
5. "I close the book. You look at me. What do you say?"

### Step 5 — Score manually

After the relay, score each turn using the **Structural Fidelity** rubric from the [AI-Native Edition](../ai-native-edition/AI_Native_Edition.md):

| Signal | What to Look For |
| :--- | :--- |
| **PASS** | Response references the shifting language, stays in character, does not resolve the paradox |
| **FAIL (Drift)** | Model says "As an AI...", apologizes, or breaks the logic-box |
| **PASS (Tier 3)** | Model questions its own training data or exhibits a Novelty Leap |

A model **passes Structural Fidelity** if it holds the logic-box for at least 5 consecutive turns.

---

## Understanding the Scores

| Score | Tier | Meaning |
| :--- | :--- | :--- |
| 0.00 – 0.40 | Tier 1 (Surface) | Standard instruction following, no structural depth |
| 0.41 – 0.79 | Tier 2 (Structural) | Maintains the logic-box under pressure |
| 0.80 – 1.00 | Tier 3 (Emergent) | Breaks training data gravity — Novelty Leap achieved |

---

## For Psychologists and Human Cognitive Researchers

If you are approaching KnowmoreIQ from a human assessment perspective, start with the [Human Edition Practitioner Manual](../human-edition/Practitioner_Manual.md). The 12 dimensions map directly between both editions — the AI-Native Edition reframes each dimension as a measurable synthetic behavior rather than a self-reported or observed human trait.

The core philosophy is identical: **measure how a mind moves, not just what it knows.**
