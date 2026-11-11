<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/436b6836-9959-4241-b595-13be56a1e788" />AstraMind AI
Agentic Enterprise Intelligence Platform | Python • RAG • Hybrid Search • Local LLM
AstraMind AI is a Python-based enterprise document intelligence project. It ingests common document formats, indexes text chunks, retrieves relevant evidence using semantic and lexical search, and uses a locally hosted LLM through Ollama to generate grounded answers.
LLM runtime: Ollama (local). This repository's documented setup uses Ollama; no cloud LLM API is required.

Application Preview
The following preview images are illustrative UI mockups created to show the intended AstraMind AI experience. They are not screenshots captured from a running application. Values, activity counts, and example responses shown in the mockups are demonstration content and should not be treated as measured project results.
1. Enterprise dashboard
   <img width="1672" height="941" alt="AstraMind AI Intelligence Dashboard-1" src="https://github.com/user-attachments/assets/95100415-2685-48ba-b619-668e6835cd93" />




2. RAG chat, citations, and local Ollama status
<img width="1672" height="941" alt="AstraMind AI Enterprise Dashboard-2" src="https://github.com/user-attachments/assets/78cf701b-6e50-4460-8acc-d3dafb026973" />

3. Chat answer and supporting evidence
<img width="1672" height="941" alt="AstraMind AI Enterprise RAG Dashboard-3" src="https://github.com/user-attachments/assets/862ded06-9698-48c0-9f54-7491d583d51f" />

The account email shown in the UI mockups (vishalus307@gmail.com) is display text supplied for this portfolio design. The current starter application does not implement user authentication or account management.
Core capabilities
- Multi-format document ingestion: PDF, DOCX, TXT, Markdown, and CSV.
- Configurable text chunking with overlap.
- Local embeddings using Sentence Transformers.
- Persistent vector storage using ChromaDB.
- Hybrid retrieval combining vector similarity and BM25 lexical search.
- Reciprocal Rank Fusion (RRF) to combine retrieval rankings.
- Optional cross-encoder reranking.
- Grounded answer generation through a locally hosted Ollama model.
- Source labels and retrieved evidence excerpts in responses.
- Controlled arithmetic calculator tool using a restricted AST parser.
- FastAPI endpoints for ingestion, questions, feedback, health, and metrics.
- Streamlit user interface.
- Retrieval evaluation using Recall@5 and Mean Reciprocal Rank (MRR).
- Basic request latency, error, and feedback counters.
Architecture
                    User
                     |
                     v
              Streamlit UI
                     |
                     v
                FastAPI
                     |
             Agent / Router
                /       \
               v         v
          RAG Pipeline  Calculator
               |
               v
         Hybrid Retrieval
          /           \
         v             v
   Vector Search     BM25 Search
         \             /
          v           v
       Reciprocal Rank Fusion
                  |
                  v
          Optional Reranking
                  |
                  v
          Retrieved Evidence
                  |
                  v
          Ollama Local LLM
                  |
                  v
        Grounded Answer + Sources
Technology stack
Area	Technology
Language	Python
API	FastAPI
UI	Streamlit
Local LLM runtime	Ollama
Example LLM	llama3.2:3b
Embeddings	Sentence Transformers
Vector database	ChromaDB
Lexical retrieval	BM25 (rank-bm25)
Ranking fusion	Reciprocal Rank Fusion
Optional reranking	Sentence Transformers CrossEncoder
Document parsing	pypdf, python-docx
HTTP client	httpx
Tests	pytest
Container	Docker


Project structure
AstraMind-AI/
├── app/
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
├── ui/
│   └── streamlit_app.py
├── evals/
│   ├── dataset.jsonl
│   └── run_eval.py
├── tests/
│   └── test_core.py
├── sample_docs/
│   ├── security_policy.md
│   └── incident_response.md
├── screenshots/
│   ├── astramind-dashboard-ollama.png
│   ├── astramind-chat-ollama.png
│   └── astramind-evidence-ollama.png
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
Prerequisites
- Windows 10/11, macOS, or Linux.
- Python 3.11 or newer.
- Git (for cloning the repository).
- Ollama installed and running.
- Enough free disk space for Python dependencies, PyTorch, the embedding model, and the selected local LLM.
Setup on Windows
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AstraMind-AI.git
cd AstraMind-AI
2. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
If PowerShell blocks activation for this terminal session:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
3. Install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
The first installation of Sentence Transformers may download PyTorch and model dependencies. The embedding model is downloaded on first use.
4. Install and start Ollama
Install Ollama from:

https://ollama.com/download

Pull the example model:
ollama pull llama3.2:3b
Check that it is available:
ollama list
Ollama normally runs as a background service on Windows. If it is not running, start it with:
ollama serve
5. Configure environment variables
Create a local .env file:
Copy-Item .env.example .env
Use these settings for the example Ollama model:
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
RERANK_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
Keep .env private. Never commit API keys, credentials, or private documents.
6. Start the FastAPI backend
In terminal 1:
uvicorn app.main:app --reload --port 8000
Useful endpoints:
- API health: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs
- Runtime metrics: http://127.0.0.1:8000/metrics
7. Start the Streamlit frontend
In terminal 2, activate the same virtual environment and run:
streamlit run ui/streamlit_app.py
Open:

http://localhost:8501
8. Try the sample documents
Upload these files through the Streamlit sidebar:
- sample_docs/security_policy.md
- sample_docs/incident_response.md
Click Index documents, then ask questions such as:
- How should an employee report a suspected phishing email?
- What happens after a security incident is identified?
- What are the requirements for accessing company systems?
The answer should be based on retrieved document context. Verify the displayed citations against the uploaded source files.
API endpoints
Method	Endpoint	Purpose
GET	/health	Health status and indexed chunk count
POST	/ingest	Upload and index documents
POST	/ask	Ask a question against indexed documents
POST	/feedback	Save answer feedback
GET	/metrics	Request and feedback counters


Example question request:
{
  "question": "How should an employee report a suspected phishing email?",
  "top_k": 5
}
Tests and retrieval evaluation
Run unit tests:
python -m pytest tests/ -v
After indexing the sample documents, run retrieval evaluation:
python -m evals.run_eval
The included evaluation script reports Recall@5 and MRR against the expected source names in evals/dataset.jsonl. These are retrieval metrics, not a complete measure of answer correctness or faithfulness. Add a larger, human-reviewed evaluation dataset before making performance claims.
Docker
Build the API image:
docker build -t astramind-ai .
Run the API container:
docker run --env-file .env -p 8000:8000 -v astramind_data:/app/data astramind-ai
The Ollama endpoint must be reachable from the container. On Docker Desktop for Windows, configure the host address appropriately (often http://host.docker.internal:11434/v1) rather than assuming localhost inside the container points to the Windows host.
Security and production considerations
This is a portfolio starter, not a production-certified enterprise system. Before using sensitive enterprise data, implement and test:
- User authentication and role-based authorization.
- Document-level access controls and tenant isolation.
- Upload size limits, file validation, and malware scanning.
- Rate limiting and request quotas.
- Prompt-injection defenses and strict treatment of retrieved documents as untrusted data.
- Audit logging, secret management, and secure deployment configuration.
- Human review and robust evaluation of generated answers.
Future improvements
- Query rewriting and multi-step retrieval.
- Conversation history and persistent chat sessions.
- OCR and table-aware parsing for scanned documents.
- Async ingestion jobs and background workers.
- Advanced answer evaluation for faithfulness and citation correctness.
- Streaming responses.
- Multi-user access control.
- OpenTelemetry tracing and token/latency monitoring.
- Scalable vector storage using pgvector or Qdrant.
Author
Vishal Bhat
Aspiring Gen AI and AI Engineer
Interests: Generative AI, AI Engineering, Python, Retrieval-Augmented Generation, LLM applications, and Agentic AI.
