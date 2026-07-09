from decimal import Decimal

class Account:
    def __init__(self, _balance=0.00):
        if _balance < 0:
            raise ValueError("Začetna vrednost ne sme biti manjša kot 0")
        self._balance = Decimal(str(_balance))

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if not isinstance(amount,(int,Decimal)):
            raise TypeError("THE AMOUNT ITS NOT RIGHT TYPE")
        elif amount <= 0:
            raise ValueError("Amount can not be less then 0")
        self._balance = self._balance + amount

    def withdraw(self, amount):
        if not isinstance(amount,(int,Decimal)):
            raise TypeError("THE AMOUNT ITS NOT RIGHT TYPE")
        elif amount <= 0:
            raise ValueError("Amount can not be less then 0")
        elif amount > self._balance:
            raise ValueError("You can not withdraw more than you have")
        self._balance = self._balance - amount
