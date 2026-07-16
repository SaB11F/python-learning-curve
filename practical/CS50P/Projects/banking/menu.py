from account import Account
from decimal import Decimal, InvalidOperation
from CoinFlip import CoinFlip
from Dice import Dice

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
                try:
                    igra = CoinFlip(uporabnik)
                    amount = Decimal(input("Buy in amount:"))

                    while True:
                        side = str(input("Heads or Tails:"))
                        side = side.lower()
                        if side not in ("heads", "tails"):
                            print("Fallse input")
                        else:
                            break

                    coin, won, nagrada = igra.generate(amount, side)

                    print(f"Toss: {coin}")

                    if won == True:
                        print(f"You won {nagrada}")
                    elif won == False:
                        print(f"GG go next")

                except ValueError as e:
                    print(e)
                except InvalidOperation:
                    print("that is not a number")

                print(f"Trenutno stanje: {uporabnik.balance}")

            case 4:
                #dice
                try:
                    igra = Dice(uporabnik)
                    amount = Decimal(input("Buy in amount:"))

                    while True:
                        num = int(input("Insert a number from one to six:"))
                        if num != 1 or 2 or 3 or 4 or 5 or 6:
                            print("false input")
                        else:
                            break

                    dice, won, nagrada = igra.generate(amount, num)
                    
                    print(f"Dice Toss: {dice}")

                    if won == True:
                        print(f"You won {nagrada}")
                    elif won == False:
                        print(f"GG go next")

                except ValueError as e:
                    print(e)
                except InvalidOperation:
                    print("that is not a number")

                print(f"Trenutno stanje: {uporabnik.balance}")

            case _:
                print("za vse ostalo")

    except ValueError:
        print(f" is not an integer")