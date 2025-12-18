# --- MODELES ---
from datetime import date
from typing import Optional, List

from pydantic import BaseModel, Field
from fastapi import File

class BigramRequest(BaseModel):
    text: str = Field(..., description="Texte saisie par l'utilisateur")

class BigramResponse(BaseModel):
    word: Optional[List[str]] = Field(default=None,description="Suggestions de mot")