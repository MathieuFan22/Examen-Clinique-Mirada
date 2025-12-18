import string
from rapidfuzz import process, distance

class CorrecteurMalagasy:
    def __init__(self, data_corpus):
        print("Chargement du Tontolo Malagasy en mémoire...")
        try:
            with open(data_corpus, 'r', encoding='utf-8') as f:
                contenu = f.read().lower()
                self.dictionnaire = list(set(mot for mot in contenu.split() if mot.isalpha()))
            
            print(f"Dictionnaire prêt : {len(self.dictionnaire)} mots chargés.")
        except FileNotFoundError:
            print("Erreur : Le fichier corpus est introuvable.")
            self.dictionnaire = []

    def suggerer(self, mot_saisi):
        if not self.dictionnaire:
            return []
        
        mot_saisi = mot_saisi.lower().strip()
        
        # Si le mot est correct, pas de suggestions
        if mot_saisi in self.dictionnaire:
            return []
        
        len_mot = len(mot_saisi)
        
        # Élargir la fenêtre de longueur pour plus de candidats
        candidats = [m for m in self.dictionnaire if abs(len(m) - len_mot) <= 3]
        
        # Si pas assez de candidats, on prend tout le dictionnaire
        if len(candidats) < 10:
            candidats = self.dictionnaire
        
        # Obtenir les 3 meilleurs résultats SANS seuil minimum
        resultats = process.extract(
            mot_saisi, 
            candidats, 
            scorer=distance.Levenshtein.normalized_similarity,
            limit=3 
        )
        
        # Retourner les 3 suggestions peu importe le score
        suggestions = [res[0] for res in resultats]
        return suggestions

# --- TEST ---

if __name__ == '__main__':
    mon_correcteur = CorrecteurMalagasy('../resources/bible.txt')

    print("\n--- DEBUT DU TEST (tape 'stop' pour quitter) ---")

    while True:
        mot_utilisateur = input("\nEntrez un mot malgache : ")

        if mot_utilisateur.lower() == 'stop':
            print("Fin du test.")
            break

        suggestions = mon_correcteur.suggerer(mot_utilisateur)

        if suggestions:
            print(f"❌ Mot inconnu. Suggestions : {suggestions}")
        else:
            print(f"✅ '{mot_utilisateur}' est correct.")