from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import process_legal_query  # Import the function from services.py

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_legal_question(request: QueryRequest):
    try:
        return process_legal_query(request.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
