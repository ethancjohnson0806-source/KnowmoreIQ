"""
KnowmoreIQ Scoring Engine
Computes 12‑dimension scores (0–10 each) from a test log.
"""

import json
import numpy as np

# Definition of the 12 dimensions (original framework)
DIMENSIONS = [
    "Pattern Recognition",
    "Multi‑Variable Pattern Integration",
    "Abstraction",
    "Rule Inference",
    "Rule Adaptation",
    "Complexity Load Management",
    "Constraint Reasoning",
    "Strategic Thinking",
    "Meta‑Reasoning",
    "Error Detection & Correction",
    "Ambiguity Tolerance",
    "Transfer Ability"
]

def compute_score(log_file_path):
    """
    log_file_path: JSON file containing list of tasks with keys:
        task_id, response, expected, dimensions, time_taken, stability_flag
    Returns dict of dimension scores.
    """
    with open(log_file_path, 'r') as f:
        log = json.load(f)
    
    # Aggregate per dimension
    dim_scores = {dim: [] for dim in DIMENSIONS}
    
    for entry in log:
        for dim in entry.get('dimensions', []):
            # Basic scoring: 1 if correct, 0 if incorrect, plus speed/stability modifiers
            correct = 1 if entry['correct'] else 0
            speed_bonus = 0
            if entry.get('time_taken', 0) < 3:   # fast response threshold
                speed_bonus = 0.2
            stability_bonus = entry.get('stability_flag', 0)   # 0 or 0.2
            task_score = correct + speed_bonus + stability_bonus
            # clamp to 0-1
            task_score = min(1.0, max(0.0, task_score))
            dim_scores[dim].append(task_score)
    
    # Average per dimension and scale to 0-10
    final_scores = {}
    for dim, scores in dim_scores.items():
        avg = np.mean(scores) if scores else 0.0
        final_scores[dim] = round(avg * 10, 1)
    
    return final_scores

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) != 2:
        print("Usage: python score_engine.py <log_file.json>")
        sys.exit(1)
    scores = compute_score(sys.argv[1])
    print(json.dumps(scores, indent=2))
