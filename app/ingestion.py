import csv, io, hashlib
from pathlib import Path
from pypdf import PdfReader
from docx import Document
from app.config import settings

SUPPORTED = {".pdf", ".docx", ".txt", ".md", ".csv"}

def extract_text(filename: str, raw: bytes) -> str:
    ext = Path(filename).suffix.lower()
    if ext not in SUPPORTED:
        raise ValueError(f"Unsupported file type: {ext}")
    if ext == ".pdf":
        return "\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(raw)).pages)
    if ext == ".docx":
        return "\n".join(p.text for p in Document(io.BytesIO(raw)).paragraphs)
    if ext == ".csv":
        return "\n".join(" | ".join(row) for row in csv.reader(io.StringIO(raw.decode("utf-8", errors="ignore"))))
    return raw.decode("utf-8", errors="ignore")

def chunk_text(text: str, size=None, overlap=None):
    size = size or settings.chunk_size
    overlap = settings.chunk_overlap if overlap is None else overlap
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("Require size > overlap >= 0")
    words, chunks, start = text.split(), [], 0
    while start < len(words):
        end = min(start + size, len(words))
        chunk = " ".join(words[start:end]).strip()
        if chunk: chunks.append(chunk)
        if end == len(words): break
        start = end - overlap
    return chunks

def make_id(source, index, content):
    return hashlib.sha256(f"{source}:{index}:{content}".encode()).hexdigest()
