# AstraMind AI — Agentic Enterprise Intelligence Platform

A substantial Python GenAI portfolio project: document ingestion, local embeddings, persistent vector search, BM25 + vector hybrid retrieval, reciprocal-rank fusion, optional reranking, grounded LLM answers with citations, controlled calculator tool, FastAPI, Streamlit, feedback and retrieval evaluation.

## Architecture

```text
Documents -> Parser -> Chunker -> Local Embeddings -> ChromaDB
                                             |
Question -> Agent Router -> Hybrid Retrieval (Vector + BM25)
                                             |
                                  Optional Cross-Encoder
                                             |
                               Grounded LLM + Citations
                                             |
                                FastAPI -> Streamlit UI
```

## Run locally

1. Python 3.11+ recommended.
2. `python -m venv .venv` then activate it.
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`.
5. Configure an OpenAI-compatible LLM endpoint. For Ollama, run a model locally and use `LLM_BASE_URL=http://localhost:11434/v1`, `LLM_API_KEY=ollama`, and `LLM_MODEL=llama3.1`. The first embedding run downloads the Sentence Transformers model.
6. Start API: `uvicorn app.main:app --reload --port 8000`
7. In another terminal: `streamlit run ui/streamlit_app.py`
8. Upload documents in the UI, then ask questions. API docs: `http://localhost:8000/docs`.

## Features
- PDF, DOCX, TXT, Markdown and CSV ingestion.
- Configurable chunking and metadata.
- Local Sentence Transformers embeddings and persistent ChromaDB.
- Hybrid retrieval with BM25 and vector similarity, combined using reciprocal-rank fusion.
- Optional cross-encoder reranking.
- Evidence-constrained RAG with inline source IDs and source excerpts.
- Controlled calculator tool (safe AST parser; no `eval` or arbitrary code execution).
- FastAPI endpoints for ingest, ask, feedback, health and metrics.
- Streamlit user interface.
- Retrieval evaluation using Recall@5 and MRR.
- Prompt-injection-aware instructions and abstention when no evidence is found.

## API
- `GET /health`
- `POST /ingest` multipart `files`
- `POST /ask` JSON `{"question":"...", "top_k":5}`
- `POST /feedback`
- `GET /metrics`

## Evaluate
Add JSONL rows to `evals/dataset.jsonl` with `question` and `expected_source`, index the sample documents, then run `python -m evals.run_eval`.

## Docker
`docker build -t astramind-ai .`
`docker run --env-file .env -p 8000:8000 -v astramind_data:/app/data astramind-ai`

## Production hardening roadmap
Add tenant isolation and document ACLs, OCR and table extraction, async ingestion queue, streaming, persistent conversation state, managed pgvector/Qdrant, OpenTelemetry tracing, cost dashboards, human-reviewed answer evaluation, and approval-gated enterprise tools. Do not expose confidential documents without access controls.

## Resume entry
**AstraMind AI — Agentic Enterprise Intelligence Platform | Python, FastAPI, RAG, ChromaDB, Sentence Transformers, BM25, Streamlit, LLM APIs**
- Built a document intelligence platform with multi-format ingestion, semantic and lexical hybrid search, and grounded LLM responses with source citations.
- Implemented configurable chunking, local embeddings, reciprocal-rank fusion, optional cross-encoder reranking, and evidence-based abstention.
- Developed REST APIs, interactive UI, controlled tool execution, feedback capture, runtime metrics, and retrieval evaluation using Recall@K and MRR.

Only claim features you have run and validated. This is a portfolio implementation, not a security-certified enterprise system.
