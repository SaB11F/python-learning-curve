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
#več metod si lahko pogledaš tukaj - https://www.w3schools.com/python/python_strings.aspž

#Imamo še par fint, ki jih lahko uporabimo pri klicanju metod in sicer:

#tukaj smo kar inline dodali metodo pri sami deklaraciji vrednosti spremenljivke
p = "rene kolednik".title()
print(f"to je p: {p}")

#ista finta, eventualy lahko tukaj dodamo kolikor metod želimo, vse inline zato, da je bolj pregledno.
r = "    rene kolednik   ".strip().title()
print(f"tukaj imamo r: {r}")
