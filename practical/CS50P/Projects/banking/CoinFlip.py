from account import Account
import random

class CoinFlip():
    def __init__(self, account, payout=2):
        self.account = account
        self.payout = payout

    def flip(self):
        obrat = random.choice(["heads", "tails"])
        return obrat
    
    def play(self, amount, side):
        #take the bet
        
        self.account.withdraw(amount)

        machine = self.flip()
        nagrada = None

        if machine == side:
            nagrada = amount * self.payout
            self.account.deposit(nagrada)
            won = True
        else:
            won = False

        return (machine, won, nagrada)