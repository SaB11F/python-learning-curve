import random
from Game import Game

class Dice(Game):
    valid_choices = (1,2,3,4,5,6)

    def __init__(self, account, payout=6):
        super().__init__(account, payout)

    def generate(self):
        obrat = random.randint(1,6)
        return obrat