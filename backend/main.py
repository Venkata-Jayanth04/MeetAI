from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
import shutil

# ==========================
# ASR
# ==========================
from asr.transcribe import transcribe_audio

# ==========================
# NLP
# ==========================
from nlp.sentiment import analyze_sentiment
from nlp.summarizer import summarize_text
from nlp.action_items import extract_action_items
from nlp.ner import extract_entities

# ==========================
# RAG
# ==========================
from rag.text_splitter import split_text
from rag.vector_store import (
    add_to_vector_db,
    reset_vector_db
)
from rag.rag_chat import rag_chat


# ==========================
# FASTAPI
# ==========================
app = FastAPI(
    title="MeetAI",
    description="AI Meeting Intelligence Assistant",
    version="1.0.0"
)

# ==========================
# CORS
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# GLOBAL TRANSCRIPT STORAGE
# ==========================
current_transcript = ""


# ==========================
# CHAT REQUEST MODEL
# ==========================
class ChatRequest(BaseModel):
    question: str


# ==========================
# HOME
# ==========================
@app.get("/")
def home():
    return {
        "message": "MeetAI Backend Running"
    }


# ==========================
# UPLOAD AUDIO
# ==========================
@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    global current_transcript

    # Create uploads directory
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # ==========================
    # TRANSCRIBE
    # ==========================
    transcript = transcribe_audio(
        file_path
    )

    current_transcript = transcript

    # ==========================
    # SENTIMENT
    # ==========================
    sentiment = analyze_sentiment(
        transcript
    )

    # ==========================
    # SUMMARY
    # ==========================
    summary = summarize_text(
        transcript
    )

    # ==========================
    # ACTION ITEMS
    # ==========================
    action_items = extract_action_items(
        transcript
    )

    # ==========================
    # NER
    # ==========================
    entities = extract_entities(
        transcript
    )

    # ==========================
    # RAG INDEXING
    # ==========================
    chunks = split_text(
        transcript
    )

    reset_vector_db()

    add_to_vector_db(
        chunks
    )

    return {
        "status": "success",
        "filename": file.filename,
        "transcript": transcript,
        "summary": summary,
        "sentiment": sentiment,
        "action_items": action_items,
        "entities": entities
    }


# ==========================
# CHAT WITH MEETING
# ==========================
@app.post("/chat")
async def chat(request: ChatRequest):

    global current_transcript

    if not current_transcript:
        return {
            "error": "Please upload a meeting first."
        }

    answer = rag_chat(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }


# ==========================
# HEALTH CHECK
# ==========================
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }