from fastapi import APIRouter, HTTPException
from app.models.correction_model import CorrectionRequest, CorrectionResponse
# On importe l'instance du correcteur déjà initialisée
from app.api.utils.processor import correcteur_malagasy 

router = APIRouter()

@router.post("/check-spelling", response_model=CorrectionResponse, description="Vérifie l'orthographe d'un mot malgache")
def check_spelling(request: CorrectionRequest):
    """
    Reçoit un mot et renvoie si il est correct ou propose des suggestions.
    """
    try:
        word_to_check = request.word
        
        # Appel à ta méthode 'suggerer' du fichier original
        suggestions = correcteur_malagasy.suggerer(word_to_check.lower())
        
        # Si la liste est vide, c'est que le mot est correct (selon ta logique)
        is_correct = len(suggestions) == 0
        
        return CorrectionResponse(
            word=word_to_check,
            is_correct=is_correct,
            suggestions=suggestions
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la correction : {e}")