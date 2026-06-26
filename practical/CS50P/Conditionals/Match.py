#Match is eventualy only thing that is kind of unknown to me
#Orther stuff is just logical parameters such as +, -, *, / and %
#Next to it come other operators such as "or", "and"
#and functions such as if, elif, else


x = int(input("Vpiši vrednost x:"))

y = x % 2

match y:
    case 1:
        print("x je liho število")
    case _:
        print("x je sodo število")