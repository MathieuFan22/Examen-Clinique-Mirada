import re
from collections import defaultdict, Counter
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
corpus_path = os.path.join(current_dir, '..', '..', '..', '..', 'resources', 'bible.txt')


# Chargement et nettoyage du corpus
def load_corpus(file_path: str) -> list:
    """
    Prétraitement :
    - passage en minuscules
    - suppression des caractères spéciaux
    - tokenisation par espace
    """
    with open(file_path, encoding="utf-8") as file:
        text = file.read().lower()

    # Conserver uniquement les lettres (compatibles Malagasy)
    text = re.sub(r"[^a-zàâéèêëïîôùûçñ\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.split()

# Entraînement du modèle Bigram
def train_bigram_model(tokens: list) -> dict:
    """
    Le modèle apprend les fréquences de transition :
    mot_i -> mot_(i+1)
    """
    model = defaultdict(Counter)

    for i in range(len(tokens) - 1):
        current_word = tokens[i]
        next_word = tokens[i + 1]
        model[current_word][next_word] += 1

    return model

tokens = load_corpus(corpus_path)
model = train_bigram_model(tokens)

# Prédiction du mot suivant
def predict_next_word(word: str, model: dict, top_k: int = 3) -> list:
    if word not in model:
        return []

    # Retourner les top_k mots les plus fréquents
    return [w for w, _ in model[word].most_common(top_k)]

def main():
    # Chargement du corpus
    tokens = load_corpus("../resources/bible.txt")

    # Entraînement du modèle
    bigram_model = train_bigram_model(tokens)

    # Boucle interactive
    while True:
        word = input("Mot : ").strip().lower()

        if word == "exit":
            print("Fin du programme.")
            break

        suggestions = predict_next_word(word, bigram_model)

        if suggestions:
            print("Suggestions :", ", ".join(suggestions))
        else:
            print("Aucune suggestion disponible.")

if __name__ == "__main__":
    main()
