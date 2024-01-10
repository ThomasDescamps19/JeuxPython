def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

def verifier_victoire(plateau, symbole):
    # Vérifier les lignes et colonnes
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return True

    # Vérifier les diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    tour = 0

    while True:
        afficher_plateau(plateau)
        symbole = symboles[tour % 2]
        position = raw_input("Joueur {} - Entrez la position (ligne,colonne) : ".format(symbole)).split(",")

        try:
            ligne, colonne = map(int, position)
        except ValueError:
            print("Veuillez entrer des coordonnées valides.")
            continue

        if 0 <= ligne < 3 and 0 <= colonne < 3 and plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = symbole

            if verifier_victoire(plateau, symbole):
                afficher_plateau(plateau)
                print("Le joueur {} a gagné!".format(symbole))
                break

            if all(plateau[i][j] != " " for i in range(3) for j in range(3)):
                afficher_plateau(plateau)
                print("Match nul!")
                break

            tour += 1
        else:
            print("Position invalide. Réessayez.")

if __name__ == "__main__":
    morpion()
