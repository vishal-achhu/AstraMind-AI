import time,json
from pathlib import Path
from fastapi import FastAPI,UploadFile,File,HTTPException
from app.schemas import AskRequest,FeedbackRequest
from app.ingestion import extract_text,chunk_text,make_id,SUPPORTED
from app.vectorstore import add_documents,count_documents
from app.agent import answer_question
from app.metrics import record_request,record_feedback,snapshot

app=FastAPI(title="AstraMind AI",version="1.0.0")

@app.get("/health")
def health(): return {"status":"ok","indexed_chunks":count_documents()}

@app.post("/ingest")
async def ingest(files:list[UploadFile]=File(...)):
    output=[]
    for file in files:
        name=file.filename or "upload"
        if Path(name).suffix.lower() not in SUPPORTED: raise HTTPException(400,f"Unsupported file: {name}")
        raw=await file.read(); text=extract_text(name,raw); chunks=chunk_text(text)
        ids=[make_id(name,i,c) for i,c in enumerate(chunks)]
        metas=[{"source":name,"chunk":i} for i in range(len(chunks))]
        if chunks: add_documents(ids,chunks,metas)
        output.append({"filename":name,"chunks":len(chunks)})
    return {"ingested":output,"total_indexed_chunks":count_documents()}

@app.post("/ask")
async def ask(payload:AskRequest):
    start=time.perf_counter(); failed=False
    try: return await answer_question(payload.question,payload.top_k)
    except Exception as exc:
        failed=True
        raise HTTPException(500,f"Request failed: {type(exc).__name__}; check API logs and LLM configuration.") from exc
    finally: record_request((time.perf_counter()-start)*1000,failed)

@app.post("/feedback")
def feedback(payload:FeedbackRequest):
    Path("data").mkdir(exist_ok=True)
    with open("data/feedback.jsonl","a",encoding="utf-8") as f: f.write(json.dumps(payload.model_dump())+"\n")
    record_feedback(payload.rating)
    return {"saved":True}

@app.get("/metrics")
def metrics(): return snapshot()
