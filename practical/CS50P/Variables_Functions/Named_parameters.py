#funkcija print() ima neke standardne parametre, ki jih drži

# *objects -> vstavimo lahko kolikor koli parametrov želimo
# sep -> seperator, basicly razdeli parametra*?
# end -> je zadnji parameter, ki se izvede ob klicu funkcije, predpostavljen je z osnovno vrednostjo
# '\n' -> "new line" vrednosti, ki te premakne v novo vrstico

#te osnovne parametre lahko manipuliramo - še posebaj end parameter
#še posebaj pri zadevi kot je naš prejšnji problem iz datoteke Multiple function parameters
#kjer vbistvu dekleriramo več parametrov, in problem tam je izpis presledka 

name = "Rene"

#V spodnjem primeru se prikaže prav
print("osnova", end=" ")
print(name)

#V tem primeru se ne
print("osnova")
print(name)