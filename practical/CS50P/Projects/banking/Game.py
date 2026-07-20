from account import Account
from abc import ABC, abstractmethod
import random
from decimal import Decimal

#če je lahko za abstract mmethod tudi kakšen drugi abstract parameter
#lahko bi uporabo attrs

class Game(ABC):
    def __init__(self, account : Account, payout: int) -> None:
        self.account = account
        self.payout = payout

    @abstractmethod
    def generate(self) -> str | int:
        ...
    
    def play(self, amount:Decimal, side:str | int) -> tuple[str | int, bool, Decimal | None]:
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
    def valid_choices(self) -> tuple[str, ...] | tuple[int, ...]:
        ...                     #elipsis, basicly empty place holder

    def describe_choices(self) -> str:
        parts = []
        for i in self.valid_choices:
            parts.append(str(i))

        return "/".join(parts)