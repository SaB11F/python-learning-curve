from account import Account
from decimal import Decimal

#SIMPLE MENU
def menu(uporabnik):
    try:
        print("0=quit, 1=deposit, 2=withdraw, 3=gamble")
        x = int(input("Vpiši x:"))

        match x:
            case 0:
                return True
            case 1:
                #deposit
                try:
                    denar = Decimal(input("Koliko denarja bi rad položil:"))
                    uporabnik.deposit(denar)
                    print(f"Trenutno stanje: {uporabnik.balance}")
                except ValueError as e:
                    print(e)
            case 2:
                #withdraw
                try:
                    denar = Decimal(input("Koliko bi rad dvignil:"))
                    uporabnik.withdraw(denar)
                    print(f"Trenutno stanje: {uporabnik.balance}")
                except ValueError as e:
                    print(e)
            case 3:
                #Gamble it away
                print("in dev")
            case _:
                print("za vse ostalo")

    except ValueError:
        print(f" is not an integer")