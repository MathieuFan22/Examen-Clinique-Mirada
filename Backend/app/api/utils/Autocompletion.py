from collections import Counter
from app.api.utils.Bigram import load_corpus
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
corpus_path = os.path.join(current_dir, '..', '..', '..', '..', 'resources', 'bible.txt')
tokens = load_corpus(corpus_path)
vocabulary = Counter(tokens)

# Construction du vocabulaire (autocomplétion)
def build_vocabulary(tokens: list) -> Counter:
    """
    Construit un vocabulaire : mot → fréquence
    """
    return Counter(tokens)

def autocomplete(prefix: str, vocabulary: Counter, top_k: int = 5) -> list:
    """
    Autocomplétion basée sur le préfixe du mot
    Exemple :
    "andri" → ["andriamanitra", "andriamanitrao", ...]
    """
    prefix = prefix.lower()

    matches = {
        word: freq
        for word, freq in vocabulary.items()
        if word.startswith(prefix)
    }

    sorted_words = sorted(matches.items(), key=lambda x: x[1], reverse=True)

    return [word for word, _ in sorted_words[:top_k]]

def main():
    # Chargement du corpus
    tokens = load_corpus("../resources/bible.txt")

    # Construction des modèles
    vocabulary = build_vocabulary(tokens)

    while True:
        prefix = input("Début du mot : ").strip().lower()

        if prefix == "exit":
            print("Fin du programme.")
            break

        suggestions = autocomplete(prefix, vocabulary)

        if suggestions:
            print("Suggestions :", ", ".join(suggestions))
        else:
            print("Aucune suggestion trouvée.")

if __name__ == "__main__":
    main()
