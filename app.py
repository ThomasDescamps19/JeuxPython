# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def reset_game():
    global nbr_secret
    nbr_secret = random.randint(1, 100)

reset_game()  # Appel initial pour définir le nombre secret au démarrage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_guess')
def check_guess():
    user_input = int(request.args.get('user_input'))
    if user_input == nbr_secret:
        return 'Correct !'
    elif nbr_secret > user_input:
        return 'Trop petit'
    else:
        return 'Trop grand'

@app.route('/reset_game')
def reset_game_route():
    reset_game()
    return jsonify({'status': 'success', 'message': 'Jeu réinitialisé'})

if __name__ == '__main__':
    app.run(debug=True)
