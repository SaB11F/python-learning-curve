from account import Account
from Game import Game
import random

class CoinFlip(Game):
    def __init__(self, account, payout=2):
        super().__init__(account, payout)

    def generate(self):
        obrat = random.choice(["heads", "tails"])
        return obrat