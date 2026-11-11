from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    chroma_dir: str = "./data/chroma"
    collection_name: str = "astramind_knowledge"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    chunk_size: int = 900
    chunk_overlap: int = 150
    llm_base_url: str = "http://localhost:11434/v1"
    llm_api_key: str = "ollama"
    llm_model: str = "llama3.1"
    llm_temperature: float = 0.1
    retrieval_candidates: int = 12
    rerank_enabled: bool = False
    rerank_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
