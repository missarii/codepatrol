from pydantic import BaseModel
from typing import Optional

class CodeSubmitRequest(BaseModel):
    username: str
