#Simple Input function in Python

input("Vpiši ime:")

#Zgornja funkcija deluje tako, da izpiše vsebino -> "Vpiši ime:"
#V samem CLI-ju pa potem tudi ponudi vtrišajočo črtico, ki omogoča,
#da uporabnik vpiše neko vsebino. 

#To je slab primer uporabe, zato moramo najprej vedno rezervirati spremenljivko,
#kateri potem s pomočjo funkcije input vpišemo vrednost

ime = input("Vpiši ime:")       #Sedaj, ko se ta koda izvede smo dodali vrednost spremenljivki -ime-
print("pozdravljen, " + ime)      #Izpiše vrednost spremenljivke