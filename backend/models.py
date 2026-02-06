from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from database import Base

class WikiQuiz(Base):
    __tablename__ = "wiki_quizzes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text)
    key_entities = Column(JSON)
    sections = Column(JSON)
    quiz = Column(JSON)
    related_topics = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
