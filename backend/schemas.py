from pydantic import BaseModel
from typing import Optional

class CodeSubmitRequest(BaseModel):
    username: str
    code: str

class CodeResult(BaseModel):
    score: float
    match: Optional[str] = None
