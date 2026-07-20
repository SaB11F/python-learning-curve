import random
from Game import Game
from account import Account

class Suit(Game):
    valid_choices = ("spade","karo","heart","cross")

    def __init__(self, account:Account, payout: int=4):
        super().__init__(account, payout)

    def generate(self) -> str:
        obrat = random.choice(self.valid_choices)
        return obrat