from pydantic import BaseModel
from typing import List

class CorrectionRequest(BaseModel):
    word: str

class CorrectionResponse(BaseModel):
    word: str
    is_correct: bool
    suggestions: List[str]