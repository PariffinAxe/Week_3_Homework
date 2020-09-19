import random

class Player():
    def __init__(self, player, choice=""):
        self.player = player
        self.choice = choice if choice != "" else random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
        if self.choice == "Scissors":
            self.score = -2
            self.method_1 = "Cuts"
            self.method_2 = "Decapitates"
        elif self.choice == "Paper":
            self.score=-1
            self.method_1 = "Disproves"
            self.method_2 = "Covers"
        elif self.choice == "Lizard":
            self.score=0
            self.method_1 = "Eats"
            self.method_2 = "Poisons"
        elif self.choice == "Rock":
            self.score = 1
            self.method_1 = "Crushes"
            self.method_2 = "Crushes"
        else:
            self.score = 2
            self.method_1 = "Vaporises"
            self.method_2 = "Smashes"
        
        