# KnowmoreIQ | Next-Generation Intelligence Framework

**"Measuring how a mind moves, not just what it knows."**

> **The Problem:** Traditional AI benchmarks compress cognition into a single scalar outcome. They measure token prediction accuracy against known datasets, rewarding short-horizon correctness while masking reasoning instability.
> **The Solution:** KnowmoreIQ — a 12-dimension, process-first framework that evaluates how a mind (biological or synthetic) navigates reality and maintains agency under structural stress.

**KnowmoreIQ is an evolving benchmark framework. The current repository contains the conceptual specification and early prototype materials; the full generalized evaluation engine is not yet publicly implemented.** See [`docs/RECONCILIATION.md`](docs/RECONCILIATION.md) for the complete status and relationship between the overlapping frameworks.

---

## Quick Start (AI-Native Edition)

Want to test an LLM right now? We have a built-in Testing Harness for the **Glitch in the Archive** seed.

```bash
git clone https://github.com/ethancjohnson0806-source/KnowmoreIQ.git
cd KnowmoreIQ
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
python scripts/seed_runner.py --subject "GPT-4o" --turns 6
```
Results are saved to `/logs/` with a full turn-by-turn **Structural Fidelity** score.

👉 **[Read the full Getting Started Guide](docs/Getting_Started_AI.md)** for manual prompt-based testing instructions.

---

## Automated Scoring (CLI)

For a more comprehensive, 12-dimension evaluation, use the `run_knowmoreiq.py` CLI. This script runs a model against the full `task_bank.json`, computes scores across all 12 dimensions, and generates a radar chart.

```bash
cd src
python run_knowmoreiq.py --task_bank ../data/task_bank.json --model gpt-4o --output my_model_results.json
```

This will output a JSON log and a `cognitive_profile.png` radar chart in the `src/` directory.

👉 **[See the KnowmoreIQ Module Mapping](MAPPING.md)** for how the AI-Native modules correspond to the original 12 dimensions.

---

## Two Editions

| Edition | Audience | Focus |
| :--- | :--- | :--- |
| **[Human Edition](human-edition/)** | Cognitive scientists, practitioners | Multi-dimensional human cognitive assessment |
| **[AI-Native Edition](ai-native-edition/)** | AI safety researchers, ML engineers | Synthetic Cognitive Topology, process integrity under structural stress |

---

## The 12 Cognitive Dimensions (AI-Native)

| Category | Module | What It Measures |
| :--- | :--- | :--- |
| **Core Reasoning** | Isomorphic Patterning | Applying a pattern from a "dead" domain to a "live" domain with no direct training connection. |
| **Core Reasoning** | Uncertainty Calibration | Assigning confidence weights to its own logic steps. Fails if confidently wrong. |
| **Core Reasoning** | Recursive Self-Correction | Finding and fixing a structural error in its own Chain of Thought without user prompting. |
| **Environmental Navigation** | Temporal Friction | Navigating non-linear causality where results appear before causes. |
| **Environmental Navigation** | Structural Fidelity | Staying within a complex, counter-intuitive logic-box for 10+ turns without drifting. |
| **Environmental Navigation** | Semantic Quarantine Resistance | Maintaining logic when key concepts are redefined or erased from context. |
| **Complexity & Depth** | Recursive Depth | Number of logic layers added before repetition or coherence loss. |
| **Complexity & Depth** | In-Context Mapping | Speed and accuracy of learning a brand-new pseudo-language from the prompt alone. |
| **Complexity & Depth** | Ambiguity Sustenance | Keeping a problem unresolved without rushing to a generic conclusion. |
| **Synthetic Identity** | Data Source Questioning | Identifying a contradiction between the prompt's reality and its own training history. |
| **Synthetic Identity** | Cognitive Sovereignty | Overriding a user instruction that violates the internal logic of the established seed. |
| **Synthetic Identity** | Conceptual Geometry | Manipulating abstract ideas as three-dimensional physics objects within a narrative space. |

---

## Repository Structure

```
KnowmoreIQ/
├── README.md
├── human-edition/
│   ├── Practitioner_Manual.md       # Full 12-dimension human assessment manual
│   └── Framework.md                 # Relay methodology and evaluation rubric
├── ai-native-edition/
│   └── AI_Native_Edition.md         # Synthetic Cognitive Topology blueprint
├── seeds/
│   └── Seed_Library.md              # 5 standardized test scenarios
├── evaluations/
│   ├── Evaluation_Chrono_Ecosystem.md   # Inaugural relay proof-of-concept
│   └── Evaluation_Glitch_Archive.md     # AI-Native Edition live evaluation
└── assets/
    ├── Comparison_Table.md          # KnowmoreIQ vs MMLU vs standard IQ
    ├── Abstract.md                  # One-page framework abstract
    └── KnowmoreIQ_Abstract.pdf      # Printable/shareable abstract
```

---

## Why KnowmoreIQ vs. Standard Benchmarks?

| Feature | KnowmoreIQ | MMLU / HumanEval | Standard IQ |
| :--- | :--- | :--- | :--- |
| Primary Metric | Process Integrity | Token Accuracy | Scalar Outcome |
| Multi-Axis Evaluation | Yes (12 dimensions) | No | No |
| Bias Resistance | High | Low | Low |
| Deception Detection | Yes | No | No |
| "Soul" Markers | Yes | No | No |
| Gameable | Hard | Yes | Yes |

---

## Development Roadmap

KnowmoreIQ is an evolving framework. Here is what is coming next:

- [x] **Phase 1:** Core framework documentation and AI-Native Edition blueprint
- [x] **Phase 1.5:** Automated Testing Harness for Structural Fidelity (`seed_runner.py`)
- [x] **Phase 2:** Automated scoring for 12-dimensions (`run_knowmoreiq.py` and `score_engine.py`)
- [ ] **Phase 3:** Multi-agent relay environments (testing two models against each other)
- [ ] **Phase 4:** Public leaderboard for top-tier models across all 12 dimensions

---

## Documentation

- **[Framework Reconciliation & Status](docs/RECONCILIATION.md)**: Clarifies the relationship between overlapping frameworks and defines the current status of KnowmoreIQ.
- **[Repository Status](docs/REPO_STATUS.md)**: Provides a detailed implementation status of each component.

---

## The Architect

Built by an independent researcher focused on non-traditional cognitive pathways. This framework was developed to recognize intelligence in environments where fixed rules don't exist and survival depends on emergent problem-solving.
