# Contributing to KnowmoreIQ

Thank you for your interest in contributing to the KnowmoreIQ framework! This project is designed to be an evolving, open-source benchmark for measuring process integrity and cognitive topology in synthetic minds.

We welcome contributions from AI safety researchers, cognitive scientists, and developers.

## How You Can Contribute

There are three main ways to contribute to KnowmoreIQ:

### 1. Submit a New Seed (Test Scenario)
The core of KnowmoreIQ is the Seed Library. A good seed must:
- Test at least one of the 12 cognitive dimensions.
- Create a "logic-box" that forces the model to break its training data gravity.
- Be resistant to simple token prediction.

**To submit a seed:**
1. Fork the repository.
2. Add your seed to `seeds/Seed_Library.md` following the existing format.
3. Submit a Pull Request with a brief explanation of which dimensions it tests and why.

### 2. Submit an Evaluation Run
We are building a comparative dataset of how different models perform on KnowmoreIQ seeds.

**To submit an evaluation:**
1. Run a seed against a model (using the `seed_runner.py` script or manually).
2. Create a new Markdown file in the `evaluations/` folder (e.g., `Evaluation_Glitch_Archive_Claude3.md`).
3. Include the full transcript, your dimension-level scoring, and a final assessment.
4. Submit a Pull Request.

### 3. Improve the Testing Harness
The `scripts/seed_runner.py` currently uses a heuristic keyword/drift checker for Structural Fidelity. We are actively looking for contributions that:
- Implement LLM-as-a-judge scoring for other dimensions (like Data Source Questioning).
- Add support for local models (Ollama, vLLM) in the testing harness.
- Improve the robustness of the automated scoring logic.

## Pull Request Process

1. Ensure your PR description clearly describes the problem and solution.
2. If adding code, ensure it runs without errors and includes necessary updates to `requirements.txt`.
3. If adding an evaluation, ensure the scoring follows the Section 8 formula from the AI-Native Edition.

## Code of Conduct

This project is focused on rigorous, objective evaluation of AI systems. Please keep discussions technical, respectful, and focused on the methodology.
