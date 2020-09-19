import random

class Player():
    def __init__(self, player, choice=""):
        self.player = player
        self.choice = choice if choice != "" else random.choice(["Rock", "Paper", "Scissors"])
        if self.choice == "Rock":
            self.score=1
            self.method="Crushes"
        elif self.choice == "Paper":
            self.score=0
            self.method="Covers"
        else:
            self.score=-1
            self.method="Cuts"
        
        