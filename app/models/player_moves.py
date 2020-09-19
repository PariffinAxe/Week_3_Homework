from app.models.player import *

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    
    def play_game(self):
        total_score = self.player1.score + (3*self.player2.score)
        if total_score == -2 or total_score == -1 or total_score == 3:
            return self.player1
        elif total_score == 2 or total_score == 1 or total_score == -3:
            return self.player2
        else:
            return None

