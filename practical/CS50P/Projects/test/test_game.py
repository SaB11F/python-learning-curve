import pytest
from Game import Game
from account import Account
from CoinFlip import CoinFlip
from Dice import Dice 


class AlwaysHeads(CoinFlip):
    def generate(self):
        return "heads"
    
class AlwaysOne(Dice):
    def generate(self):
        return 1

def test_win():
    uporabnik = Account(100)

    igra = AlwaysHeads(uporabnik)
    coin, won, nagrada = igra.play(10, "heads")
    assert won is True
    assert nagrada == 20
    assert uporabnik.balance == 110

def test_lost():
    uporabnik = Account(100)

    igra = AlwaysHeads(uporabnik)
    coin, won, nagrada = igra.play(10, "tails")
    assert won is False
    assert nagrada is None
    assert uporabnik.balance == 90

def test_dice_win():
    uporabnik = Account(100)

    igra = AlwaysOne(uporabnik)
    coin, won, nagrada = igra.play(10, 1)
    assert won is True
    assert nagrada == 60
    assert uporabnik.balance == 150

def test_dice_lost():
    uporabnik = Account(100)

    igra = AlwaysOne(uporabnik)
    coin, won, nagrada = igra.play(10, 2)
    assert won is False
    assert nagrada is None
    assert uporabnik.balance == 90
    
def test_balance_unchanged():
    uporabnik = Account(100)

    igra = AlwaysOne(uporabnik)
    with pytest.raises(ValueError):
        coin, won, nagrada = igra.play(9999, 2)

    assert uporabnik.balance == 100

def test_generate():
    heads = 0
    tails = 0
    igra = CoinFlip(Account(100))

    for i in range(50):
        obrat = igra.generate()

        if obrat == "heads":
            heads += 1
        elif obrat == "tails":
            tails += 1
    
    assert heads > 0
    assert tails > 0
