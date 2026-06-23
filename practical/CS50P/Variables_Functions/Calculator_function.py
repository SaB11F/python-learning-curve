#Obvezno moreš deklerirat, da je intput INT tipa -> celo številskega

def main():
    x = int(input("Vpiši vrednost x:"))
    print(f"koren števila {x} je: {square(x)}")

def square(num):
    return num * num

main()
