from account import Account
from Game import Game
import random

class CoinFlip(Game):
    valid_choices = ("heads", "tails")

    def __init__(self, account:Account, payout: int=2):
        super().__init__(account, payout)

    def generate(self) -> str:
        obrat = random.choice(self.valid_choices)
        return obrat