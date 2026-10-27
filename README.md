# eval-suite

Evaluation of [rag-compliance](https://github.com/laurahmaza/rag-compliance),
a citation-verifying RAG over the NIST AI RMF 1.0.

Project 3 of a 12-week AI evals portfolio: golden set, rubric, human labels,
then a validated LLM-as-judge and a reproducible red-teaming battery.

> Built with AI-assisted tooling (Cursor, ChatGPT and an AI assistant) under my direction; all design decisions, risk judgments and validation conclusions are my own.

## Contents
- `golden/golden_v1.jsonl`: golden set, 69 cases (schema and process in `golden/README.md`)
- `golden/CRITERIA.md`: gold-answer writing criteria
- `rubric/rubric.md`: scoring rubric (not written yet)
- `labels/`: human labels (ground truth for judge validation)
- `tests/`: schema tests, run in CI

## Reproduce
```
python -m pytest
```

## Limitations
- **Single labeler.** All 69 gold answers were reviewed by one person (the author). No inter-annotator agreement (Cohen's kappa) has been measured yet.
- **Rules were written during labeling, not before.** Writing criteria in `golden/CRITERIA.md` evolved while labeling and were applied retroactively to every reviewed case. This is a deviation from writing labeling rules before labeling. The criteria are frozen as of v1 for all future cases.
- **Size.** 69 cases, below the target of 100 hand-labeled cases and the 150-300 planned for the full set.
- **Category imbalance.** single_doc 35, multi_doc 14, unanswerable 12, adversarial 8.
- **One corpus.** All cases come from NIST AI RMF 1.0; results do not generalize to other documents.
- **No rubric yet**, so no scores are reported.
