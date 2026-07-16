import random
from Game import Game

class Suit(Game):
    valid_choices = ["spade","karo","heart","cross"]

    def __init__(self, account, payout=4):
        super().__init__(account, payout)

    def generate(self):
        obrat = random.choice(self.valid_choices)
        return obrat