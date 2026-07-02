from calc import calc
import pytest

def test_positive():
    assert calc(2) == 4
    assert calc(3) == 9

def test_negative():
    assert calc(-2) == 4
    assert calc(-3) == 9

def test_zero():
    assert calc(0) == 0

def test_str():
    with pytest.raises(TypeError):
        calc("mace")