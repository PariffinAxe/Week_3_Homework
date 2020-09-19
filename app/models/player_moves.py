from app.models.player import *

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = ""
        self.method = ""
        self.loser = ""

    
    def play_game(self):
        total_score = self.player1.score + (5*self.player2.score)
        if total_score == -9 or total_score == -8 or total_score == -7 or total_score == -5 or total_score == -2 or total_score == 1 or total_score == 4 or total_score == 7 or total_score == 9 or total_score == 10:
            self.winner = self.player1
        elif total_score == -11 or total_score == -10 or total_score == -3 or total_score == -4 or total_score == -1 or total_score == 2 or total_score == 3 or total_score == 5 or total_score == 8 or total_score == 11:
            self.winner = self.player2
        else:
            self.winner = None
        if total_score %2 == 0 and self.winner:
            self.method = self.winner.method_2
        elif total_score %2 != 0 and self.winner:
            self.method = self.winner.method_1
        if self.winner == self.player1:
            self.loser = self.player2
        elif self.winner == self.player2:
            self.loser = self.player1

