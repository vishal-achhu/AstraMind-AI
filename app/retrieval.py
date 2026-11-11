from collections import defaultdict
from rank_bm25 import BM25Okapi
from app.config import settings
from app.vectorstore import vector_search, collection

def lexical_search(query, n=12):
    data = collection().get(include=["documents","metadatas"])
    docs, metas, ids = data.get("documents") or [], data.get("metadatas") or [], data.get("ids") or []
    if not docs: return []
    bm25 = BM25Okapi([d.lower().split() for d in docs])
    scores = bm25.get_scores(query.lower().split())
    order = sorted(range(len(scores)), key=lambda i:scores[i], reverse=True)[:n]
    return [{"id":ids[i],"text":docs[i],"metadata":metas[i],"lexical_score":float(scores[i])} for i in order if scores[i] > 0]

def hybrid_search(query, top_k=5):
    n = max(settings.retrieval_candidates, top_k)
    fused = defaultdict(lambda: {"score":0.0})
    for ranked in (vector_search(query,n), lexical_search(query,n)):
        for rank, hit in enumerate(ranked,1):
            fused[hit["id"]]["score"] += 1/(60+rank)
            fused[hit["id"]].update(hit)
    return sorted(fused.values(), key=lambda x:x["score"], reverse=True)[:top_k]
