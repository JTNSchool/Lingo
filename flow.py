from Lingo import *
from Data import *
from Bingo import *

EvenGetallen = True
    
PrintKaart, BingoKaart = MaakNieuwKaart(EvenGetallen)
ballenbak = MaakBallenBak(PrintKaart, BingoKaart)

Antwoord, PrintWoord, VorigeWoorden = MaakNieuwWoord()
Word = ""
while True:
    Scherm(Word, PrintWoord, VorigeWoorden)
    PrintWoord, Word = RaadWoord(Antwoord)
    VorigeWoorden.append(PrintWoord)
    
    if Word == Antwoord:
        print('goed, je mag een bal pakken!')
        PrintKaart, BingoKaart, ballenbak = PakEenBal(PrintKaart, BingoKaart, ballenbak)
        HeeftBingo = KijkVoorBingo(PrintKaart, BingoKaart)
        if HeeftBingo:
            print('Je wint je hebt bingo')
            exit()
        RodeBallen, GroeneBallen = KrijgAantalBallen(ballenbak)
        CheckBallen(RodeBallen, GroeneBallen)
        input("Druk op enter om door te gaan")
        Antwoord, PrintWoord, VorigeWoorden = MaakNieuwWoord()
        
    elif len(VorigeWoorden) >= RAADAANTAL+1:
        input(f"Helaas je hebt dit woord niet geraden het woord was {Antwoord}. Druk op enter om door te gaan.")
        Antwoord, PrintWoord, VorigeWoorden = MaakNieuwWoord()
        

    
    