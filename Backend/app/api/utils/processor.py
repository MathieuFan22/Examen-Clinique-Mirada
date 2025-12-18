import os
from pathlib import Path
from app.api.utils.Autocompletion import build_vocabulary, autocomplete
from app.api.utils.Bigram import load_corpus
from app.api.utils.correcteur_orthographique import CorrecteurMalagasy

# On récupère le chemin absolu de 'processor.py'
current_file = Path(__file__).resolve() 


ROOT_DIR = current_file.parents[2]

CORPUS_PATH = os.path.join(ROOT_DIR, '..', '..', "resources", "bible.txt")

print(f"\n--- Vérification du chemin ---")
print(f"Racine détectée : {ROOT_DIR}")
print(f"Fichier cherché : {CORPUS_PATH}")

try:
    if not os.path.exists(CORPUS_PATH):
        raise FileNotFoundError(f"Le fichier n'existe pas à l'emplacement indiqué.")

    # Chargement
    tokens = load_corpus(CORPUS_PATH)
    vocabulary = build_vocabulary(tokens)
    correcteur_malagasy = CorrecteurMalagasy(CORPUS_PATH)
    
    print("✅ Initialisation réussie.")

except Exception as e:
    print(f"❌ ERREUR : {e}")
    vocabulary = {}
    correcteur_malagasy = None

# Fonctions utilitaires pour tes endpoints
def get_autocomplete_suggestions(prefix: str, top_k: int = 5):
    return autocomplete(prefix, vocabulary, top_k) if vocabulary else []

def get_spelling_suggestions(word: str):
    return correcteur_malagasy.suggerer(word) if correcteur_malagasy else []