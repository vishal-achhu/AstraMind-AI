import json
from pathlib import Path
from app.retrieval import hybrid_search
def main():
    rows=[json.loads(x) for x in Path(__file__).with_name("dataset.jsonl").read_text().splitlines() if x.strip()]
    if not rows: print("No evaluation examples."); return
    recall=[]; reciprocal=[]
    for row in rows:
        hits=hybrid_search(row["question"],5); expected=row["expected_source"]
        ranks=[i for i,h in enumerate(hits,1) if expected.lower() in h.get("metadata",{}).get("source","").lower()]
        recall.append(float(bool(ranks))); reciprocal.append(1/ranks[0] if ranks else 0)
        print(row["question"],"->",bool(ranks))
    print(f"Recall@5: {sum(recall)/len(recall):.3f}")
    print(f"MRR@5: {sum(reciprocal)/len(reciprocal):.3f}")
if __name__=="__main__": main()
