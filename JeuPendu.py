import random

def choisir_mot():
    mots = ["python", "java", "ruby", "javascript", "html", "css", "php"]
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def jeu_pendu():
    while True:
        mot_a_deviner = choisir_mot()
        lettres_trouvees = []
        tentatives_max = 6
        tentatives = 0

        print("Bienvenue dans le jeu du pendu!")

        while tentatives < tentatives_max:
            mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
            print("Mot actuel: {}".format(mot_cache))

            proposition = raw_input("Devinez une lettre : ")

            if proposition in lettres_trouvees:
                print("Vous avez déjà deviné cette lettre. Essayez encore.")
                continue

            lettres_trouvees.append(proposition)

            if proposition not in mot_a_deviner:
                tentatives += 1
                print("Incorrect! Il vous reste {} tentatives.".format(tentatives_max - tentatives))

            if "_" not in afficher_mot_cache(mot_a_deviner, lettres_trouvees):
                print("Félicitations! Vous avez deviné le mot: {}".format(mot_a_deviner))
                break

        if tentatives == tentatives_max:
            print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était: {}".format(mot_a_deviner))

        rejouer = raw_input("Voulez-vous rejouer ? (Oui/Non) : ").lower()
        if rejouer != 'oui':
            break

if __name__ == "__main__":
    jeu_pendu()
