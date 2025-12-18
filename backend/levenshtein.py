from rapidfuzz import process, distance

class CorrecteurMalagasy:
    def __init__(self, data_corpus):
        # print("Chargement du Tontolo Malagasy en mémoire...")
        try:
            with open(data_corpus, 'r', encoding='utf-8') as f:
                # On utilise un set pour éliminer les doublons, puis on trie
                contenu = f.read().lower()
                # On ne garde que les mots qui ne contiennent pas de chiffres
                self.dictionnaire = list(set(mot for mot in contenu.split() if mot.isalpha()))
            
            print(f"Dictionnaire prêt : {len(self.dictionnaire)} mots chargés.")
        except FileNotFoundError:
            print("Erreur : Le fichier corpus est introuvable.")
            self.dictionnaire = []

    def suggerer(self, mot_saisi):
        """
        Retourne les meilleures suggestions pour un mot mal orthographié.
        """
        if not self.dictionnaire:
            return []

        mot_saisi = mot_saisi.lower().strip()

        # 1. Si le mot est déjà dans le dictionnaire, pas besoin de correction
        if mot_saisi in self.dictionnaire:
            return []

        # 2. Pré-filtrage : on ne compare qu'avec les mots de longueur proche (+/- 2 lettres)
        # Cela évite de calculer Levenshtein sur tout le dictionnaire inutilement
        len_mot = len(mot_saisi)
        candidats = [m for m in self.dictionnaire if abs(len(m) - len_mot) <= 2]

        # 3. Utilisation de RapidFuzz sur les candidats
        # On utilise Levenshtein normalisé pour avoir un score entre 0 et 100
        resultats = process.extract(
            mot_saisi, 
            candidats, 
            scorer=distance.Levenshtein.normalized_similarity,
            limit=3 # On propose les 3 meilleurs mots
        )

        # 4. On filtre les résultats (score > 60 pour éviter les suggestions absurdes)
        suggestions = [res[0] for res in resultats if res[1] >= 60]
        
        return suggestions

# --- EXEMPLE D'UTILISATION ---
# Remplacez 'votre_corpus.txt' par votre vrai fichier
mon_correcteur = CorrecteurMalagasy('votre_corpus.txt')

# Simulation d'une saisie utilisateur dans votre éditeur
mot_utilisateur = "fhavanana" 
suggestions = mon_correcteursuggerer(mot_utilisateur)

if suggestions:
    print(f"Mot inconnu. Suggestions : {suggestions}")
else:
    print("Mot correct.")