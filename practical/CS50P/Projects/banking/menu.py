from account import Account
from decimal import Decimal, InvalidOperation
from CoinFlip import CoinFlip
from Dice import Dice
from Suit import Suit
from Game import Game

def play_game(game:Game) -> None:
    possibilities = game.describe_choices()

    print(f"Choose {possibilities}:")

    lookup = {}

    for i in game.valid_choices:
        key = str(i).lower()
        lookup[key] = i

    while True:
        bet = input("What u bet on:").strip().lower()
        if bet not in lookup:
            print("Fallse input")
        else:
            input_value = lookup[bet]
            break

    try:
        amount = Decimal(input("Buy in amount:"))

        outcome, won, nagrada = game.play(amount, input_value)

        print(f"Result: {outcome}")

        if won == True:
            print(f"You won {nagrada}")
        elif won == False:
            print(f"GG go next")

    except ValueError as e:
        print(e)
    except InvalidOperation:
        print("this is not a number")

    print(f"Trenutno stanje: {game.account.balance}")

#SIMPLE MENU
def menu(uporabnik: Account) -> bool | None:
    try:
        print("0=quit, 1=deposit, 2=withdraw, 3=CoinFlip, 4=Dice, 5=Cards")
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
                igra:Game = CoinFlip(uporabnik)
                play_game(igra)
            case 4:
                igra = Dice(uporabnik)
                play_game(igra)
            case 5:
                igra = Suit(uporabnik)
                play_game(igra)
            case _:
                print("za vse ostalo")

    except ValueError:
        print(f" is not an integer")

    return False