# Golden set — construction criteria

Status: draft, to be completed in Week 6.

- Source corpus: NIST AI RMF 1.0 chunks from rag-compliance (`corpus/nist_ai_rmf.yaml`).
- Schema: id, query, gold_answer, gold_citations, answerable, category, difficulty, source, notes.
- Categories: single_doc, multi_doc, unanswerable, adversarial.
- Discard rule: drop any example whose answer cannot be verified with an exact corpus
  citation, or that has two contradictory correct answers.
- TODO: sampling and stratification rationale, target size (150-300), labeling process.
