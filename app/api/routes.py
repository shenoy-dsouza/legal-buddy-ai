from fastapi import APIRouter, HTTPException, status
from app.models.schemas import QueryRequest, QueryResponse
from app.services.query_processor import fetch_answer

router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
def ask_legal_question(request: QueryRequest):
    try:
        return fetch_answer(request.question)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
