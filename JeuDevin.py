# JeuDevin.py

import random

def run_game():
    nbr_secret = random.randint(1, 100)
    INVITE = 'Propose un nombre entre 1 et 100 :'

    while True:
        try:
            nbr_joueur = int(raw_input(INVITE))
            if nbr_joueur == nbr_secret:
                return 'Correct !'
            elif nbr_secret > nbr_joueur:
                print('Trop petit')
            else:
                print('Trop grand')
        except ValueError:
            print("Veuillez entrer un nombre entier.")
