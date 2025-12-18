# **Rapport de Projet \- Editeur de texte Malagasy**

## **Examen Clinique TP Intelligence Artifiielle**

Réalisé au sein de ISPM - Madagascar (www.ispm-edu.com)

### **1\. Informations sur le Groupe**

Liste de tous les membres de l'équipe ayant participé au TP.

#### Membre 1 :
* nom : ANDRIANANDRAINA
* prénom(s) : Anja Fanirintsoa Mathieu
* classe : ISAIA 5
* numéro : 02
* rôle : Front-End

#### Membre 2 : 
* nom : HARIMALALA
* prénom(s) : Mendrika Henintsoa
* classe : IGGLIA 5
* numéro : 06
* rôle : Autocomplétion (Next Word Prediction) et API

#### Membre 3 :
* nom : ANDRIAMANANA
* prénom(s) : Aina Sariaka
* classe : IGGLIA 5
* numéro : 09
* rôle : Correcteur Orthographique et API

#### Membre 4 : 
* nom : ANDRIANTSOA
* prénom(s) : Safidy Herinirina Arindranto
* classe : IGGLIA 5
* numéro : 19
* rôle : Récupération des données, Scrapping, Lemmatisation

#### Membre 5 : 
* nom : RAKOTOARISOA
* prénom(s) : Finaritra Onintsoa
* classe : ISAIA 5
* numéro : 06
* rôle : Vérification à base de règles


### **2\. Résumé du Travail**

Un éditeur de texte spécialisé pour la langue malagasy, intégrant des outils avancés de Traitement Automatique des Langues (TAL/NLP) pour garantir une rédaction fluide et sans fautes.

**Fonctionnalités Clés :**  
* Correcteur Orthographique : * Moteur basé sur la distance de Levenshtein et des tables de hachage pour des suggestions rapides.
* Vérification de Règles (REGEX) : Détection automatique des erreurs de formation de mots interdites en malagasy (ex: séquences nb, mk, etc.) via des automates cellulaires/REGEX.
* Lemmatisation (Fandrasan-teny) : Analyse morphologique permettant de retrouver la racine d'un mot (ex: manosika → tosika).
* Autocomplétion : Prédiction du mot suivant (Next Word Prediction) pour accélérer la saisie.

  **Stack Technique**
  * Langage :
      - Backend : Python
      - Frontend : React, Draft.js
  * Algorithmique :
      - Distance de Levenshtein
      - N-grams

**Objectif du projet**
Pallier le manque d'outils numériques pour la langue malagasy en proposant une solution capable de comprendre les spécificités de sa morphologie et de sa syntaxe.

**Lien util**
https://github.com/Rohan29-AN/rakibolana_malagasy.git

### **5\. Bibliographie**

* Cours Algorithme avancée M1 (Distance de Levenshtein)







