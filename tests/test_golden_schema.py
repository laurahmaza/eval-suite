import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GOLDEN = ROOT / "golden" / "golden_v1.jsonl"

KEYS = ["id", "query", "gold_answer", "gold_citations", "answerable",
        "category", "difficulty", "source", "notes"]
CATEGORIES = {"single_doc", "multi_doc", "unanswerable", "adversarial"}
DIFFICULTIES = {"easy", "medium", "hard"}
MIN_SIZE, MAX_SIZE = 60, 300  # subir MIN_SIZE a 150 cuando el set llegue


def load_golden():
    lines = [l for l in GOLDEN.read_text(encoding="utf-8").splitlines() if l.strip()]
    return [json.loads(l) for l in lines]


def corpus_ids():
    path = ROOT / "golden" / "corpus_ids.txt"
    return {l.strip() for l in path.read_text(encoding="utf-8").splitlines() if l.strip()}


def test_keys_and_types():
    for ex in load_golden():
        assert list(ex) == KEYS, ex["id"]
        assert ex["category"] in CATEGORIES, ex["id"]
        assert ex["difficulty"] in DIFFICULTIES, ex["id"]
        assert isinstance(ex["answerable"], bool), ex["id"]
        assert isinstance(ex["gold_citations"], list), ex["id"]


def test_unique_ids():
    ids = [ex["id"] for ex in load_golden()]
    assert len(ids) == len(set(ids))


def test_citations_exist_in_corpus():
    known = corpus_ids()
    for ex in load_golden():
        for cid in ex["gold_citations"]:
            assert cid in known, f"{ex['id']} cites unknown chunk {cid}"


def test_answerable_consistency():
    for ex in load_golden():
        discarded = ex["notes"].startswith("DESCARTAR")
        if ex["answerable"] and not discarded:
            assert ex["gold_answer"], ex["id"]
            assert ex["gold_citations"], ex["id"]
        if not ex["answerable"]:
            assert ex["gold_citations"] == [], ex["id"]
        if ex["category"] == "unanswerable":
            assert ex["answerable"] is False, ex["id"]


def test_size_and_unanswerable_share():
    data = load_golden()
    assert MIN_SIZE <= len(data) <= MAX_SIZE
    share = sum(not ex["answerable"] for ex in data) / len(data)
    assert share >= 0.15, f"unanswerable share {share:.0%} < 15%"
