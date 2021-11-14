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
    return sub

def compare_submission(code: str, submission_id: int):
    db = SessionLocal()
    submissions = db.query(CodeSubmission).filter(CodeSubmission.id != submission_id).all()
    db.close()
    return compare_all(code, submissions)
