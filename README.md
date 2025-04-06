# Générateur et Bruteforce de Mots de Passe (Python)

Ce projet est un petit programme Python en ligne de commande qui propose plusieurs outils liés aux mots de passe :

- Génération de mots de passe (sécurisés ou personnalisés)
- Bruteforce basique (génération de combinaisons)
- Lecture de fichiers `.txt` ou bruteforce de fichiers `.zip`
- Interface simple et intuitive pour s'entraîner à la manipulation de chaînes et de fichiers

---

## Fonctions disponibles

### 1. Générer un mot de passe sécurisé (RGPD)
Crée automatiquement un mot de passe aléatoire de 12 caractères contenant :
- Lettres minuscules et majuscules
- Chiffres
- Caractères spéciaux

> Le mot de passe est également enregistré dans un fichier `mdp.txt`.

---

### 2. Générer un mot de passe personnalisé
Permet à l'utilisateur de :
- Choisir la longueur du mot de passe
- Choisir les types de caractères à inclure (minuscules, majuscules, chiffres, symboles)

---

### 3. Bruteforce basique
Génère **toutes les combinaisons possibles** de mots de passe d'une certaine longueur avec des lettres minuscules (`a-z`) et les écrit dans un fichier `brutForce.txt`.

>  Cette méthode ne teste pas réellement un mot de passe, elle sert surtout d'exemple de récursion et peut être très lente.

---

### 4. Lecture et test de fichiers `.txt` ou `.zip`
-  **.txt** : Affiche le contenu du fichier ligne par ligne
-  **.zip** : Tente de déchiffrer un fichier ZIP protégé par un mot de passe, en testant chaque ligne d'un fichier dictionnaire fourni par l'utilisateur
