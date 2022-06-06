from flask import render_template

from app import app 
from models.player import Player
from models.game import game

@app.route("/")
def index():
    return render_template("index.html", title = "Home")
    
@app.route("/<choice1>/<choice2>")
def play(choice1, choice2):
    player1 = Player("Player 1", choice1)
    player2 = Player("Player 2", choice2)
    msg = game(player1, player2)
    return render_template("result.html", title1 = "Home", msg = msg )