from functools import lru_cache
from app.config import settings

@lru_cache(maxsize=1)
def model():
    from sentence_transformers import CrossEncoder
    return CrossEncoder(settings.rerank_model)

def rerank(query, hits):
    if not settings.rerank_enabled or not hits: return hits
    scores = model().predict([(query,h["text"]) for h in hits])
    ranked = []
    for hit, score in zip(hits,scores):
        item = dict(hit); item["rerank_score"] = float(score); ranked.append(item)
    return sorted(ranked,key=lambda x:x["rerank_score"],reverse=True)
