# 🧠 AstraMind AI
### Agentic Enterprise Intelligence Platform | Generative AI | RAG | Python

AstraMind AI is an intelligent enterprise knowledge platform designed to transform unstructured company documents into searchable, evidence-backed knowledge.

Built using Python and Generative AI technologies, the platform combines Retrieval-Augmented Generation (RAG), hybrid search, vector databases, LLM integration, and controlled AI tool execution to deliver contextual and source-grounded responses.

The goal is to build a reliable enterprise AI assistant that can retrieve information, understand complex queries, and assist users with knowledge-intensive tasks.

---

## 🚀 Key Features

- **Multi-Format Document Processing:** Upload and process PDF, DOCX, TXT, Markdown, and CSV files.
- **Retrieval-Augmented Generation (RAG):** Generate answers using relevant information retrieved from uploaded documents.
- **Semantic Search:** Understand the meaning and context of user queries using embedding models.
- **Hybrid Search:** Combine vector similarity search with BM25 lexical retrieval.
- **Reciprocal Rank Fusion:** Combine multiple retrieval rankings to improve search relevance.
- **LLM Integration:** Generate contextual responses using locally hosted or OpenAI-compatible language models.
- **Source Citations:** Display supporting document references alongside generated answers.
- **Optional Reranking:** Improve retrieval relevance using cross-encoder reranking.
- **AI Tool Execution:** Includes a controlled arithmetic calculator tool.
- **Feedback System:** Capture user ratings and comments.
- **Evaluation Framework:** Measure retrieval performance using Recall@K and Mean Reciprocal Rank.
- **Monitoring:** Track API requests, errors, latency, and feedback statistics.

---

## 🏗️ System Architecture

```text
                 USER
                   |
                   v
          STREAMLIT FRONTEND
                   |
                   v
             FASTAPI BACKEND
                   |
          AGENT / QUERY ROUTER
                   |
          +--------+---------+
          |                  |
          v                  v
     RAG PIPELINE       CALCULATOR
          |
          v
     HYBRID RETRIEVAL
          |
     +----+------+
     |           |
     v           v
  VECTOR       BM25
  SEARCH       SEARCH
     |           |
     +-----+-----+
           |
           v
    RECIPROCAL RANK FUSION
           |
           v
     OPTIONAL RERANKING
           |
           v
       CHROMADB
           |
           v
      RETRIEVED CONTEXT
           |
           v
        LLM MODEL
           |
           v
    GROUNDED RESPONSE
           |
           v
    SOURCE CITATIONS
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Frontend | Streamlit |
| LLM Integration | Ollama / OpenAI-compatible APIs |
| Embedding Models | Sentence Transformers |
| Vector Database | ChromaDB |
| Retrieval | BM25, Vector Search |
| Ranking | Reciprocal Rank Fusion |
| Reranking | Cross-Encoder |
| Document Processing | PyPDF, python-docx |
| Data Processing | Python |
| Evaluation | Recall@K, MRR |
| Containerization | Docker |
| Testing | Pytest |

---

## 📂 Project Structure

```text
AstraMind-AI/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── ingestion.py
│   ├── vectorstore.py
│   ├── retrieval.py
│   ├── rerank.py
│   ├── llm.py
│   ├── agent.py
│   └── metrics.py
│
├── ui/
│   └── streamlit_app.py
│
├── evals/
│   ├── __init__.py
│   ├── dataset.jsonl
│   └── run_eval.py
│
├── tests/
│   └── test_core.py
│
├── sample_docs/
│   ├── security_policy.md
│   └── incident_response.md
│
├── data/
│   └── (Generated locally)
│
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AstraMind-AI.git

cd AstraMind-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create your environment file:

```powershell
Copy-Item .env.example .env
```

Configure the LLM settings in `.env`:

```env
CHROMA_DIR=./data/chroma
COLLECTION_NAME=astramind_knowledge

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

CHUNK_SIZE=900
CHUNK_OVERLAP=150

LLM_BASE_URL=http://localhost:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=llama3.2:3b

LLM_TEMPERATURE=0.1

RETRIEVAL_CANDIDATES=12
RERANK_ENABLED=false
```

### 5. Install Ollama

Download Ollama:

https://ollama.com/download

Download the model:

```bash
ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

Ensure the Ollama service is running.

### 6. Start the Backend

```bash
uvicorn app.main:app --reload --port 8000
```

Backend URL:

http://localhost:8000

Interactive API documentation:

http://localhost:8000/docs

### 7. Start the Frontend

Open another terminal:

```bash
streamlit run ui/streamlit_app.py
```

Open:

http://localhost:8501

---

## 💡 How to Use AstraMind AI

1. Launch the Streamlit application.
2. Upload your enterprise documents.
3. Click **Index Documents**.
4. Enter a question related to the uploaded documents.
5. AstraMind retrieves relevant information using hybrid search.
6. The LLM generates an evidence-grounded response.
7. Review the source references and supporting excerpts.
8. Submit feedback to help assess answer quality.

---

## 🧪 Evaluation and Testing

Run automated tests:

```bash
python -m pytest tests/ -v
```

Run the retrieval evaluation:

```bash
python -m evals.run_eval
```

### Evaluation Metrics

| Metric | Purpose |
|---|---|
| Recall@K | Measures whether relevant documents appear in the top K results |
| MRR | Measures the ranking position of the first relevant result |

The evaluation dataset can be extended with additional questions and expected source documents.

---

## 🔐 Security and Reliability Considerations

- Environment variables are used for configurable credentials.
- The calculator tool uses a restricted AST-based arithmetic parser rather than arbitrary code execution.
- Retrieved document content is treated as untrusted input.
- The generation prompt instructs the LLM to use supplied evidence and provide citations.
- The system is designed to abstain when relevant evidence is unavailable.

**Note:** These are initial safeguards. Production deployment requires authentication, authorization, document-level access controls, tenant isolation, rate limiting, and security testing.

---

## 🔮 Future Enhancements

- Multi-agent orchestration and task planning.
- Conversational memory and context management.
- Advanced query rewriting and decomposition.
- OCR and intelligent extraction from scanned documents.
- Document-level permissions and enterprise authentication.
- Streaming LLM responses.
- Advanced RAG evaluation and hallucination detection.
- PostgreSQL / pgvector integration.
- Redis-based asynchronous document processing.
- OpenTelemetry monitoring and observability.
- Cloud deployment and scalable infrastructure.

---

## 👨‍💻 Author

**Vishal Bhat**

B.Tech – Cyber Security

Interested in Artificial Intelligence, Generative AI, Python Development, LLM Applications, and Agentic AI Systems.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
