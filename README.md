# eval-suite

Professional-grade evaluation of [rag-compliance](https://github.com/laurahmaza/rag-compliance),
a citation-verifying RAG over the NIST AI RMF 1.0.

Project 3 of a 12-week AI evals portfolio: golden set, rubric, human labels,
then a validated LLM-as-judge and a reproducible red-teaming battery.

## Contents
- `golden/golden_v1.jsonl` — golden set (schema in `golden/README.md`)
- `rubric/rubric.md` — scoring rubric
- `labels/` — human labels (ground truth for judge validation)
- `tests/` — schema tests, run in CI

## Limitations
Work in progress. See `golden/README.md` for construction criteria and known gaps.
