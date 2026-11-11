from functools import lru_cache
import chromadb
from sentence_transformers import SentenceTransformer
from app.config import settings

@lru_cache(maxsize=1)
def embedder():
    return SentenceTransformer(settings.embedding_model)

@lru_cache(maxsize=1)
def collection():
    client = chromadb.PersistentClient(path=settings.chroma_dir)
    return client.get_or_create_collection(settings.collection_name, metadata={"hnsw:space":"cosine"})

def add_documents(ids, texts, metadatas):
    vectors = embedder().encode(texts, normalize_embeddings=True).tolist()
    collection().upsert(ids=ids, documents=texts, metadatas=metadatas, embeddings=vectors)

def vector_search(query, n=12):
    q = embedder().encode([query], normalize_embeddings=True).tolist()
    result = collection().query(query_embeddings=q, n_results=min(n, max(collection().count(), 1)), include=["documents","metadatas","distances"])
    return [{"id":result["ids"][0][i], "text":d, "metadata":result["metadatas"][0][i], "distance":result["distances"][0][i]} for i,d in enumerate(result["documents"][0])]

def count_documents():
    return collection().count()
