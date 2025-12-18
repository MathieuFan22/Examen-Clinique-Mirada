# --- MODELES ---
from datetime import date
from typing import Optional, List

from pydantic import BaseModel, Field
from fastapi import File



class AutocompleteRequest(BaseModel):
    text: str = Field(..., description="Texte saisie par l'utilisateur")

class AutocompleteResponse(BaseModel):
    suggestions: Optional[List[str]] = Field(default=None,description="Suggestions de mot")