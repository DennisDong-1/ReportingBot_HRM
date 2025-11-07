# ===========================================
# 📄 main.py
# HR Reporting Bot using Hugging Face API + Local HR Dataset
# ===========================================

from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_query

app = FastAPI(title="HR Reporting Bot (Hugging Face + Local DB)")

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "HR Reporting Bot is running 🚀"}

@app.post("/ask")
def ask_bot(query: Query):
    """Receive user questions and process them through the agent."""
    response = process_query(query.question)
    return {"response": response}

# Run using:
# uvicorn main:app --reload
