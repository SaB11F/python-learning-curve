while True:
    try:
        x = int(input("Vpiši nekaj:"))
    except NameError:
        print(f"{x} is not defined")
    except ValueError:
        print(f"is not and intager")
    else:
        break

print(f"x je {x}")