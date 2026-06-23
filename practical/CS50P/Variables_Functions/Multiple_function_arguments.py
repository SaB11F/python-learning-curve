#velikokrat imamo problem z " " - presledki pri funkciji za izpisovanje
#kot lahko vidimo v spodnjem primeru se dve vrednosti spremenljivke izpišeta, kot ta di bili ista vrednost,
#saj operator "+" združi dve vrednosti v 1 / oz. zgleda tako saj jih tako izpiše
#vrednosti z 2ma različnima tipoma se ne moreta združiti.

name = "Rene"
print("Moje ime je" + name)

#Izpi zgornje funkcije je -> "Moje ime jeRene" -> kar pa ne zgleda pravilno,
#zato pa lahko uporabimo operator "," ki je namenjen naštevanju vrednosti spremenljiv
#znotraj funkcije in že avtomatsko doda " " - presledek pri izpisu

print("moje ime je", name)

#moramo samo paziti, da ne bomo zapisali presledka na koncu tekstovnega tipa spremenljivke!