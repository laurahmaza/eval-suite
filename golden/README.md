# Golden set: construction and process

Status: v1, 69 cases.

- Source corpus: NIST AI RMF 1.0 chunks from rag-compliance (`corpus/nist_ai_rmf.yaml`, 50 chunks).
- Schema: id, query, gold_answer, gold_citations, answerable, category, difficulty, source, notes.
- Categories (v1 counts): single_doc 35, multi_doc 14, unanswerable 12, adversarial 8.
- Discard rule: drop any example whose answer cannot be verified with an exact corpus
  citation, or that has two contradictory correct answers.

## Labeling process
- 70 answers were drafted, then reviewed one at a time by the author with a yes/no verdict against the supporting corpus text.
- Results: 18 kept as drafted, 51 rewritten, 1 discarded (g21). 69 cases remain.
- Writing criteria: `golden/CRITERIA.md`.

## Deviations
- The writing criteria were created during labeling, not before it. Each new rule was applied retroactively to all cases already reviewed. The criteria are frozen for v1 and all later cases.

## Known gaps
- One labeler; agreement with a second independent labeler not yet measured.
- Below the target size (100 hand-labeled, 150-300 total).
- Chunks not cited by any case: org_integration, map_3, measure_4, appendixA_human_domain.
