from account import Account
import pytest

#happy path
def test_positive():
    assert Account(100).balance == 100
    assert Account(0).balance == 0
    
def test_negative():
    with pytest.raises(ValueError):
        Account(-20)

def test_deposit():
    a = Account(100)
    a.deposit(50)
    assert a.balance == 150

def test_wrong_deposit():
    a = Account(100)
    with pytest.raises(ValueError):
        a.deposit(-5)
    with pytest.raises(ValueError):
        a.deposit(0)
    
    with pytest.raises(TypeError):
        a.deposit("abc")

def test_withdraw():
    a = Account(100)
    a.withdraw(30)
    assert a.balance == 70

def test_wrong_withdraw():
    a = Account(100)
    with pytest.raises(ValueError):
        a.withdraw(0)
    with pytest.raises(ValueError):
        a.withdraw(-5)
    with pytest.raises(ValueError):
        a.withdraw(9999)
    with pytest.raises(TypeError):
        a.withdraw("abc")

#ker Account nima setter funkcije, je smiselno, da uporabnik
#ne more spremeniti vrednosti svoje belance
def test_cannot_set_balance():
    a = Account(100)
    with pytest.raises(AttributeError):
        a.balance = 999