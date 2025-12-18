from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from app.api.utils.Autocompletion import autocomplete, vocabulary
from app.models.autocomplete_model import AutocompleteResponse, AutocompleteRequest

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\asafidyherinirin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

router = APIRouter()

@router.post("/get-suggestions", response_model=AutocompleteResponse, description="Suggestion de mots pour l'utilisateur")
def get_suggestions(request: AutocompleteRequest):
    """
    Receives an image as a Base64 string and a custom Tesseract config.
    """
    try:
        text = request.text
        suggestions = autocomplete(text.lower(), vocabulary, top_k=5)
        print(suggestions)
        # Return the result
        return AutocompleteResponse(suggestions=suggestions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")