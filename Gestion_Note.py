# --- Dictionnaires des coefficients ---
coefficients = {
    "Français": 3,
    "Anglais": 2,
    "Physique": 4,
    "Mathématiques": 5,
    "Sport": 1
}

# --- Fonction pour calculer la moyenne et la mention ---
def calcul_bulletin(nom, prenom, matieres):
    somme_ponderee = 0
    somme_coeffs = 0
    for matiere in matieres:
        note = matieres[matiere]
        coeff = coefficients[matiere]
        somme_ponderee += note * coeff
        somme_coeffs += coeff
    moyenne = somme_ponderee / somme_coeffs

    if moyenne >= 16:
        mention = "Très bien"
    elif moyenne >= 14:
        mention = "Bien"
    elif moyenne >= 12:
        mention = "Assez bien"
    elif moyenne >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant"
    
    return moyenne, mention

# --- Liste pour stocker les bulletins ---
bulletins = []

# --- Fonction pour saisir un étudiant ---
def ajouter_etudiant():
    nom = input("\nNom de l'étudiant : ")
    prenom = input("Prénom de l'étudiant : ")

    matieres = {}
    for matiere in coefficients:
        while True:
            try:
                note = float(input(f"Note de {matiere} (/ 20) : "))
                if 0 <= note <= 20:
                    matieres[matiere] = note
                    break
                else:
                    print("Erreur : la note doit être entre 0 et 20.")
            except ValueError:
                print("Erreur : entre un nombre valide.")

    moyenne, mention = calcul_bulletin(nom, prenom, matieres)

    bulletin = f"\n------ Bulletin ------\nNom : {nom}\nPrénom : {prenom}\n"
    for matiere in matieres:
        bulletin += f"- {matiere} : {matieres[matiere]}/20 (Coeff {coefficients[matiere]})\n"
    bulletin += f"Moyenne pondérée : {moyenne:.2f}/20\nMention : {mention}\n----------------------\n"

    bulletins.append(bulletin)
    print("\n Étudiant ajouté avec succès !\n")

# --- Fonction pour afficher tous les bulletins ---
def afficher_bulletins():
    if not bulletins:
        print("Aucun bulletin enregistré pour l'instant.")
    else:
        print("\n===== TOUS LES BULLETINS =====")
        for bulletin in bulletins:
            print(bulletin)

# --- Fonction pour sauvegarder dans un fichier .txt ---
def sauvegarder_bulletins():
    if not bulletins:
        print("Aucun bulletin à enregistrer.")
        return
    with open("bulletins.txt", "w", encoding="utf-8") as fichier:
        for bulletin in bulletins:
            fichier.write(bulletin + "\n")
    print(" Tous les bulletins ont été enregistrés dans 'bulletins.txt'.")

# --- Menu principal ---
while True:
    print("\n========== MENU ==========")
    print("1. Ajouter un étudiant")
    print("2. Afficher tous les bulletins")
    print("3. Enregistrer les bulletins dans un fichier texte")
    print("4. Quitter")
    print("==========================")

    choix = input("Votre choix (1/2/3/4) : ")

    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        afficher_bulletins()
    elif choix == "3":
        sauvegarder_bulletins()
    elif choix == "4":
        print("Merci d'avoir utilisé le gestionnaire de notes. À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez entrer un chiffre entre 1 et 4.")