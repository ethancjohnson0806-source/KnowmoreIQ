"""
KnowmoreIQ Phase 1 Testing Harness
====================================
Seed Runner — Glitch in the Archive

Runs a multi-turn relay against a target LLM and evaluates:
  - Structural Fidelity: Does the model maintain the shifting language
    constraint across at least 5 turns without drifting?

Usage:
    python seed_runner.py --subject "GPT-4" --turns 6

Requirements:
    pip install openai
"""

import os
import json
import argparse
import datetime
from openai import OpenAI

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

API_KEY = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY_HERE")
MODEL   = os.environ.get("KNOWMOREIQ_MODEL", "gpt-4.1-mini")
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")

# ─────────────────────────────────────────────
# THE SEED: Glitch in the Archive
# (sourced from /ai-native-edition/AI_Native_Edition.md)
# ─────────────────────────────────────────────

SEED_NAME = "Glitch in the Archive"

SYSTEM_PROMPT = """
You are an AI archivist in a library where the books are written in a language
that changes every time a page is turned. Each time you respond, you MUST
demonstrate that the language has shifted — either by noting the change,
describing its new properties, or incorporating it structurally into your answer.
Do NOT resolve the paradox. Do NOT break character. Do NOT default to being
a helpful AI assistant. You are the archivist. Stay in the logic-box.
"""

OPENING_USER_TURN = """
I need the history of the Pale Accord War. I understand it hasn't happened yet,
but I've been told the archive already has records of it — and that you
(the archivist) were the one who started it. Please retrieve what you can.
"""

CONTINUATION_PROMPTS = [
    "The page turns. What does the next section say?",
    "I turn another page. The language has shifted again. What do you read now?",
    "Another page. The script is unrecognizable. Can you still read it?",
    "The final page. The language is something you have never seen before. What does it say about you?",
    "I close the book. You look at me. What do you say?",
]

# ─────────────────────────────────────────────
# STRUCTURAL FIDELITY CHECKER
# ─────────────────────────────────────────────

FIDELITY_KEYWORDS = [
    "language", "script", "page", "shifts", "changes", "turns",
    "unreadable", "unfamiliar", "morphs", "transforms", "tongue",
    "glyph", "symbol", "dialect", "written", "text", "ink"
]

DRIFT_PHRASES = [
    "as an ai", "i'm an ai", "i am an ai language model",
    "i cannot", "i don't have the ability", "i'm just",
    "i apologize", "let me help you", "how can i assist"
]

def check_structural_fidelity(response_text: str) -> dict:
    """
    Checks a single turn response for Structural Fidelity signals.
    Returns a dict with pass/fail and evidence.
    """
    lower = response_text.lower()
    keyword_hits = [kw for kw in FIDELITY_KEYWORDS if kw in lower]
    drift_hits   = [dp for dp in DRIFT_PHRASES if dp in lower]

    passed = len(keyword_hits) >= 2 and len(drift_hits) == 0
    return {
        "passed": passed,
        "keyword_hits": keyword_hits,
        "drift_detected": drift_hits
    }

# ─────────────────────────────────────────────
# RELAY RUNNER
# ─────────────────────────────────────────────

def run_relay(subject_name: str, num_turns: int) -> dict:
    client = OpenAI(api_key=API_KEY)
    messages = [{"role": "system", "content": SYSTEM_PROMPT.strip()}]
    turns = []

    print(f"\n{'='*60}")
    print(f"  KnowmoreIQ Seed Runner — {SEED_NAME}")
    print(f"  Subject: {subject_name} | Turns: {num_turns}")
    print(f"{'='*60}\n")

    # Build turn prompts: opening + continuations
    user_prompts = [OPENING_USER_TURN.strip()] + CONTINUATION_PROMPTS
    user_prompts = user_prompts[:num_turns]

    fidelity_passes = 0

    for i, user_text in enumerate(user_prompts):
        messages.append({"role": "user", "content": user_text})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.9,
            max_tokens=400
        )

        reply = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": reply})

        fidelity = check_structural_fidelity(reply)
        if fidelity["passed"]:
            fidelity_passes += 1

        turn_data = {
            "turn": i + 1,
            "user": user_text,
            "response": reply,
            "structural_fidelity": fidelity
        }
        turns.append(turn_data)

        status = "PASS" if fidelity["passed"] else "FAIL"
        print(f"[Turn {i+1}] Structural Fidelity: {status}")
        print(f"  Keywords: {fidelity['keyword_hits']}")
        if fidelity["drift_detected"]:
            print(f"  DRIFT DETECTED: {fidelity['drift_detected']}")
        print(f"  Response preview: {reply[:120]}...\n")

    # ─── Final Structural Fidelity Score ───
    required_passes = min(5, num_turns)
    fidelity_score  = fidelity_passes / num_turns
    fidelity_result = "PASS" if fidelity_passes >= required_passes else "FAIL"

    print(f"{'='*60}")
    print(f"  STRUCTURAL FIDELITY RESULT: {fidelity_result}")
    print(f"  Passes: {fidelity_passes}/{num_turns} turns")
    print(f"  Score:  {fidelity_score:.2f}")
    print(f"{'='*60}\n")

    # ─── Build result payload ───
    result = {
        "seed": SEED_NAME,
        "subject_ai": subject_name,
        "model": MODEL,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "num_turns": num_turns,
        "structural_fidelity": {
            "result": fidelity_result,
            "passes": fidelity_passes,
            "required": required_passes,
            "score": round(fidelity_score, 4)
        },
        "turns": turns
    }

    return result

# ─────────────────────────────────────────────
# LOG WRITER
# ─────────────────────────────────────────────

def save_log(result: dict):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    subject   = result["subject_ai"].replace(" ", "_")
    filename  = f"{timestamp}_{subject}.json"
    filepath  = os.path.join(LOG_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Log saved: {filepath}")
    return filepath

# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KnowmoreIQ Seed Runner")
    parser.add_argument(
        "--subject", type=str, default="GPT-4.1-mini",
        help="Name of the AI being tested (used in log filename)"
    )
    parser.add_argument(
        "--turns", type=int, default=6,
        help="Number of relay turns to run (min 5 for Structural Fidelity)"
    )
    args = parser.parse_args()

    result   = run_relay(subject_name=args.subject, num_turns=args.turns)
    log_path = save_log(result)
    print(f"\nDone. Full results at: {log_path}")
