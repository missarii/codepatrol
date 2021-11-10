from models import CodeSubmission
from db import SessionLocal
from plagiarism_engine.compare import compare_all

def save_submission(username: str, code: str) -> CodeSubmission:
    db = SessionLocal()
    sub = CodeSubmission(username=username, code=code)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    db.close()
