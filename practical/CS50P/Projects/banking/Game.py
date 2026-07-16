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
    @abstractmethod             #vody never runs, to he point, moremo ga overwriteat
    def valid_choices(self):
        ...                     #elipsis, basicly empty place holder

    def describe_choices(self):
        parts = []
        for i in self.valid_choices:
            parts.append(str(i))

        return "/".join(parts)