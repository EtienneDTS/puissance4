def afficher_grille(grille):
    for ligne in grille:
        print("|", end=" ")
        for case in ligne:
            print(case, end=" ")
        print("|")
    print("---------------")
    print("| 1 2 3 4 5 6 7 |")
    print("---------------")


def tour(grille, colonne, joueur):
    for ligne in range(5, -1, -1):
        if grille[ligne][colonne - 1] == 0:
            grille[ligne][colonne - 1] = joueur
            return True
    return False


def verifier_egalite(grille):
    for ligne in grille:
        for case in ligne:
            if case == 0:
                return False
    return True


def verifier_victoire(grille, joueur):
    # Vérifie les lignes
    for ligne in range(6):
        for colonne in range(4):
            if grille[ligne][colonne] == grille[ligne][colonne + 1] == grille[ligne][colonne + 2] == grille[ligne][colonne + 3] == joueur:
                return True

    # Vérifie les colonnes
    for colonne in range(7):
        for ligne in range(3):
            if grille[ligne][colonne] == grille[ligne + 1][colonne] == grille[ligne + 2][colonne] == grille[ligne + 3][colonne] == joueur:
                return True

    # Vérifie les diagonales (descendantes)
    for ligne in range(3):
        for colonne in range(4):
            if grille[ligne][colonne] == grille[ligne + 1][colonne + 1] == grille[ligne + 2][colonne + 2] == grille[ligne + 3][colonne + 3] == joueur:
                return True

    # Vérifie les diagonales (ascendantes)
    for ligne in range(3, 6):
        for colonne in range(4):
            if grille[ligne][colonne] == grille[ligne - 1][colonne + 1] == grille[ligne - 2][colonne + 2] == grille[ligne - 3][colonne + 3] == joueur:
                return True

    return False


def puissance4():
    grille = [[0] * 7 for i in range(6)]
    joueur = 1

    while True:
        afficher_grille(grille)

        colonne = int(
            input(f"Joueur {joueur}, choisissez une colonne (1-7): "))
        if 1 <= colonne and colonne <= 7:
            if tour(grille, colonne, joueur):
                if verifier_victoire(grille, joueur):
                    afficher_grille(grille)
                    print(f"Le joueur {joueur} remporte la partie !")
                    break
                elif verifier_egalite(grille):
                    afficher_grille(grille)
                    print("Match nul !")
                    break
                else:
                    joueur = 3 - joueur
            else:
                print("La colonne est pleine. Choisissez une autre colonne.")
        else:
            print("Choix de colonne invalide. Veuillez choisir une colonne entre 1 et 7.")


puissance4()
