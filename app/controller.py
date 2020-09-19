from flask import render_template, redirect, request
from app import app
from app.models.player_moves import *


@app.route("/")
def give_rules():
    return render_template("rules.html", title="Home")

@app.route("/Friend")
def play_a_friend():
    global player1
    global player2
    player1=""
    player2=""
    return render_template("play.html", title="Play A Friend", who="a Friend", player="1")

@app.route("/Computer")
def play_the_computer():
    global player1
    global player2
    player1=""
    player2=Player("The Computer")
    return render_template("play.html", title="Play the Computer", who="the Computer", player="1")

@app.route("/player-chosen", methods=["POST"])
def player_choice():
    global player1
    global player2
    if request.form["name"] != "":
        playerName = request.form["name"]
    elif player1 == "":
        playerName = "Player 1"
    else:
        playerName = "Player 2"
    playerChoice = request.form["selection"]
    if player1 == "":
        player1 = Player(playerName, playerChoice)
    else:
        player2 = Player(playerName, playerChoice)
    if player2 == "":
        return render_template("play.html", title="Player 2 Selection", who="a Friend", player="2")
    else:
        return redirect(f"/{player1.choice}/{player2.choice}")

@app.route("/<p1choice>/<p2choice>")
def display_results(p1choice, p2choice):
    global player1
    global player2
    game = Game(player1,player2)
    game.play_game()
    if game.winner:
        display_text = f"{game.winner.player}'s {game.winner.choice} {game.method} {game.loser.player}'s {game.loser.choice}!"
        winner_text = f"{game.winner.player} Wins!!! Care for another round?"
    else:
        display_text = f"This game is all tied up, you both chose {player1.choice}."
        winner_text = "Let's go again again and see if we can find a winner"
    return render_template("results.html", title="Results", display_text=display_text, winner_text=winner_text)

