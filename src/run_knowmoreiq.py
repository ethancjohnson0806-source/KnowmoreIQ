"""
CLI to run KnowmoreIQ test on an AI model (OpenAI, Anthropic, local, etc.)
"""

import json
import argparse
import time
from openai import OpenAI
from score_engine import compute_score, DIMENSIONS
import os

# Placeholder: replace with actual API call to your chosen model
def query_model(prompt, model_name="gpt-4o"):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def run_test(task_bank_path, model_name="gpt-4o", output_log="test_log.json"):
    with open(task_bank_path, 'r') as f:
        tasks = json.load(f)
    
    log_entries = []
    for tier in ['tier1', 'tier2', 'tier3']:
        for task in tasks[tier]:
            start = time.time()
            response = query_model(task['prompt'], model_name)
            elapsed = time.time() - start
            correct = (response.lower() == task['expected_answer'].lower())
            log_entries.append({
                "task_id": task['id'],
                "prompt": task['prompt'],
                "response": response,
                "expected": task['expected_answer'],
                "correct": correct,
                "time_taken": elapsed,
                "dimensions": task['dimensions'],
                "stability_flag": 0   # placeholder; can be derived from consecutive responses
            })
    
    with open(output_log, 'w') as f:
        json.dump(log_entries, f, indent=2)
    
    # Compute and print scores
    scores = compute_score(output_log)
    print("\n12‑Dimension Scores (0–10):")
    for dim, score in scores.items():
        print(f"  {dim}: {score}")
    
    # Optional: generate radar chart (requires matplotlib)
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Filter out dimensions not present in scores to avoid errors
        present_dimensions = [dim for dim in DIMENSIONS if dim in scores]
        
        angles = np.linspace(0, 2*np.pi, len(present_dimensions), endpoint=False).tolist()
        values = [scores[dim] for dim in present_dimensions]
        
        # Ensure the plot closes the loop
        if present_dimensions:
            values += values[:1]  
            angles += angles[:1]

        fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
        ax.fill(angles, values, alpha=0.25)
        ax.plot(angles, values, linewidth=2)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(present_dimensions, size=8)
        plt.title(f"KnowmoreIQ Cognitive Profile for {model_name}")
        plt.savefig(f"cognitive_profile_{model_name}.png")
        print(f"Radar chart saved as cognitive_profile_{model_name}.png")
    except ImportError:
        print("Matplotlib not installed – skipping radar chart. Install with `pip install matplotlib`")
    except Exception as e:
        print(f"Error generating radar chart: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task_bank", default="../data/task_bank.json", help="Path to task bank JSON")
    parser.add_argument("--model", default="gpt-4o", help="Model identifier (e.g., gpt-4o, gemini-1.5-flash)")
    parser.add_argument("--output", default="test_log.json", help="Output log file")
    args = parser.parse_args()
    
    # Ensure OPENAI_API_KEY is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set it before running the script: export OPENAI_API_KEY=\"your_key\"")
        exit(1)
        
    run_test(args.task_bank, args.model, args.output)
