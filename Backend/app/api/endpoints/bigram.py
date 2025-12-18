from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse

from app.models.bigram_model import BigramResponse, BigramRequest


# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\asafidyherinirin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

router = APIRouter()

@router.post("/get-words", response_model=BigramResponse, description="Suggestion de mots pour l'utilisateur")
def get_words(request: BigramRequest):
    """
    Receives an image as a Base64 string and a custom Tesseract config.
    """
    try:
        text = request.text
        words = []
        return BigramResponse(words=words)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")