import string
import random
import time
import zipfile
import os

# Boucle principale du programme
while True:
    print("\n--- Générateur de mots de passe ---")
    print("1 - Générer un mot de passe (RGPD)")
    print("2 - Générer un mot de passe personnalisé")
    print("3 - Bruteforce un mot de passe")
    print("4 - Lire un fichier (.txt ou .zip)")
    print("5 - Quitter")
    choix = input("Entrez votre choix (1 à 5) : ")

    # Option 1 : mot de passe sécurisé de 12 caractères
    if choix == "1":
        nb_cara = 12
        caracteres = string.ascii_letters + string.digits + "#?!;&*@"
        mdp = ''.join(random.choice(caracteres) for _ in range(nb_cara))
        print("Mot de passe généré :", mdp)

        # Enregistre le mot de passe dans un fichier
        with open("mdp.txt", "w") as fichier:
            fichier.write(mdp)

    # Option 2 : mot de passe personnalisé
    elif choix == "2":
        nb_cara = int(input("Nombre de caractères souhaités : "))

        # Choix des types de caractères à inclure
        utiliser_min = input("Inclure des minuscules ? (o/n) : ").lower() == "o"
        utiliser_maj = input("Inclure des majuscules ? (o/n) : ").lower() == "o"
        utiliser_chiffres = input("Inclure des chiffres ? (o/n) : ").lower() == "o"
        utiliser_speciaux = input("Inclure des caractères spéciaux ? (o/n) : ").lower() == "o"

        # Construction de la liste des caractères à utiliser
        liste_utilisee = ""
        if utiliser_min:
            liste_utilisee += string.ascii_lowercase
        if utiliser_maj:
            liste_utilisee += string.ascii_uppercase
        if utiliser_chiffres:
            liste_utilisee += string.digits
        if utiliser_speciaux:
            liste_utilisee += "#?!;&*@"

        # Vérifie qu'au moins un type est sélectionné
        if not liste_utilisee:
            print("Aucun type de caractère sélectionné !")
            continue

        # Génération du mot de passe
        mdp = ''.join(random.choice(liste_utilisee) for _ in range(nb_cara))
        print("Mot de passe personnalisé :", mdp)

    # Option 3 : Bruteforce (génère toutes les combinaisons possibles)
    elif choix == "3":
        # Fonction récursive pour générer les mots de passe
        def recur_mdp(liste, mot, taille):
            if len(mot) == taille:
                fichier.write(mot + "\n")
            else:
                for c in liste:
                    recur_mdp(liste, mot + c, taille)

        nb_chars = int(input("Longueur du mot de passe à brute forcer : "))
        alphabet = string.ascii_lowercase  # Alphabet utilisé (a-z)

        start = time.time()  # Chrono

        # Sauvegarde dans un fichier
        with open("brutForce.txt", "w") as fichier:
            recur_mdp(alphabet, "", nb_chars)

        duration = time.time() - start
        print(f"Bruteforce terminé en {duration:.2f} secondes.")

    # Option 4 : Lire un fichier .txt ou tester un mot de passe sur un fichier .zip
    elif choix == "4":
        chemin = input("Entrez le chemin vers le fichier .txt ou .zip : ")

        if not os.path.exists(chemin):
            print("Fichier introuvable.")
            continue

        # Lecture d'un fichier texte
        if chemin.endswith(".txt"):
            print("\n--- Contenu du fichier texte ---")
            with open(chemin, "r") as f:
                for ligne in f:
                    print(ligne.strip())

        # Lecture et test de mot de passe sur fichier ZIP
        elif chemin.endswith(".zip"):
            dictionnaire = input("Entrez le chemin du fichier .txt contenant les mots de passe : ")
            if not os.path.exists(dictionnaire):
                print("Fichier dictionnaire introuvable.")
                continue

            with zipfile.ZipFile(chemin, 'r') as zipf:
                with open(dictionnaire, 'r') as f:
                    for line in f:
                        mot_de_passe = line.strip().encode('utf-8')
                        try:
                            zipf.extractall(pwd=mot_de_passe)  # Test du mot de passe
                            print(f"✅ Mot de passe trouvé : {mot_de_passe.decode()}")
                            break
                        except:
                            continue
                    else:
                        print("❌ Aucun mot de passe n'a fonctionné.")

        else:
            print("Format non reconnu. Veuillez fournir un fichier .txt ou .zip.")

    # Option 5 : Quitter le programme
    elif choix == "5":
        print("Au revoir !")
        break

    # Autre : choix invalide
    else:
        print("Choix invalide, veuillez réessayer.")
