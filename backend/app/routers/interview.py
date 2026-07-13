from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.interview import InterviewSession, InterviewQA
from app.schemas import InterviewCreate, InterviewSessionOut, InterviewSubmission
from app.core.ai_service import AIService 

# 1. DEFINE ROUTER FIRST
router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)

# 2. THEN USE IT FOR ROUTES
@router.post("/generate", response_model=InterviewSessionOut, status_code=status.HTTP_201_CREATED)
def generate_interview(payload: InterviewCreate, db: Session = Depends(get_db)):
    # ... your logic here ...
    session = InterviewSession(...)
    # ... 
    return session

@router.post("/{session_id}/submit")
def submit_interview(session_id: int, payload: InterviewSubmission, db: Session = Depends(get_db)):
    # ... your logic here ...
    return {...}