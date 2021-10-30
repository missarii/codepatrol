from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base
from datetime import datetime

class CodeSubmission(Base):
    __tablename__ = "submissions"
