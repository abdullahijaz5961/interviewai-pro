from sqlalchemy import Column, Integer, String, DateTime
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