from calc import calc

def main():
    test_calc()

def test_calc():
    assert calc(2) == 4
    assert calc(3) == 9
    assert calc(-2) == 4
    assert calc(-3) == 9
    assert calc(0) == 0

if __name__ == "__main__":
    main()