#Data type string - is essentialy an array of charachters.
#V tem nizu karakterjev lahko izvedemo razne built in metode
#to so metode, ki so specifične samo za string data type

a = "     rene kolednik      "

print(a)

#strip() - je metoda, ki izbriše nepotrebne presledke

a = a.strip()       #pomembno je, da normaliziramo spremembo metode
print(a)

#capitalize - metoda, ki capitilizira prvo črko v nizu

a = a.capitalize()
print(a)

#title() - po drugi strani poveča obe / vse prve črke v posamezni besedi

m = "rene kolednik tretji"
m = m.title()
print(m)

#To je bilo zgolj par izmed metod, ki jih string prenese
#več metod si lahko pogledaš tukaj - https://www.w3schools.com/python/python_strings.asp
