from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class InterviewSession(Base):
    __tablename__ = "interview_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    job_title = Column(String)
    job_description = Column(String)
    overall_score = Column(Integer, nullable=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # --- ADD THIS LINE HERE ---
    qa_pairs = relationship("InterviewQA", backref="session")

class InterviewQA(Base):
    __tablename__ = "interview_qa"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"))
    question_text = Column(String)
    user_answer = Column(String, nullable=True)
    ai_feedback = Column(String, nullable=True)
    score = Column(Integer, nullable=True)