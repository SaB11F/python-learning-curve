from account import Account
import random

class Game():
    def __init__(self, account, payout=2):
        self.account = account
        self.payout = payout

    def generate(self):
        return NotImplementedError
    
    def play(self, amount, side):
        #take the bet
        
        self.account.withdraw(amount)

        machine = self.generate()
        nagrada = None

        if machine == side:
            nagrada = amount * self.payout
            self.account.deposit(nagrada)
            won = True
        else:
            won = False

        return (machine, won, nagrada)