from account import Account
from menu import menu

#rezerviramo uporabnika z začetnik accountom v vrednosti 100
uporabnik = Account(100)

while True:
    #naredit mormo loop, prva stvar ki jo loop prikaže je menu za izbiro
    #Dati moramo neko osnovno vrednost, naprimer, 100e
    #potem pa user dodaja s pomočjo metod deposit in withdraw
    #neke se more rezervirat uporabnika

    
    #SIMPLE MENU
    if menu(uporabnik):
        break


    #dodamo meni za igre itd. -> myb gambling menu posebja?


