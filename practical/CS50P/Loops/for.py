#for loop nam omogoča iteriranje skozi seznam podatkov
#torej gremo v primerjavi z while vedno skozi neki seznam in nismo več odvisni od pogoja
#ampak od določenega števila iteracij

for i in [0,1,2]:
    print(i+1)

#ker pa je to zamudno imamo še en pre made function ki je range

for i in range(10):
    print(i+10)

#maš tudi več različnih načinov kako lahko dodaš range - večlje iteracije, omejiš iteracije, 
print("range iteracije")
for i in range(2,20,2):
    print(i)

#zdaj lahko lažje izpišemo vse skupaj.

vsota = 100

for i in range(vsota):
    print(i+1000)

#kao neka finta da lahko že v pritnu dodamo for loop

print("Malica\n" * 3, end="")

#Imamo še par zanimivih načinov iz  We3Schools, ki znajo bit uporabni

fruits = ["banana","pomaranča","marelica"]      
for i in fruits:
    print(i)

#mamo tudi len()
for i in range(len(fruits)):
    print(fruits[i])

#loop skozi string

s = "Banana"
for i in s:
    print(i)

