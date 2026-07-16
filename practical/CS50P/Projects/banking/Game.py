from account import Account
from abc import ABC, abstractmethod
import random

class Game(ABC):
    def __init__(self, account, payout):
        self.account = account
        self.payout = payout

    @abstractmethod
    def generate(self):
        raise NotImplementedError
    
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
    
    @property
    @abstractmethod
    def valid_choice():