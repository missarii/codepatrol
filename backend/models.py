from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base
from datetime import datetime

class CodeSubmission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    code = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
