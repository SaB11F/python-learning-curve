import random
from Game import Game
from account import Account

class Dice(Game):
    valid_choices = (1,2,3,4,5,6)

    def __init__(self, account : Account, payout: int=6):
        super().__init__(account, payout)

    def generate(self) ->int:
        obrat = random.randint(1,6)
        return obrat