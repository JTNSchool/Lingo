from Data import *
import random
from termcolor import colored
import os
import copy

#Genereerd een nieuw bingo kaart
def MaakNieuwKaart(IsEven:bool) -> list:
    Getallen = list(range(1, 100, 2))
    if IsEven:
        Getallen = list(range(2, 100, 2))

    BingoKaart = []
    PrintKaart = []

    for _ in range(4):
        Rij = []
        for _ in range(4):
            RandomGetal = random.choice(Getallen)
            Getallen.remove(RandomGetal)
            Rij.append(RandomGetal)
        BingoKaart.append(Rij)

    PrintKaart = copy.deepcopy(BingoKaart)
    Loops = ALGERADENAANTAL
    while Loops >= 1:
        RandomRij = random.randint(0,3)
        RandomIndex = random.randint(0,3)
        if PrintKaart[RandomRij][RandomIndex] == BingoKaart[RandomRij][RandomIndex]:
            PrintKaart[RandomRij][RandomIndex] = colored(PrintKaart[RandomRij][RandomIndex], "green")
            Loops -= 1
    
    return PrintKaart, BingoKaart

#Maakt de ballenbak
def MaakBallenBak(PrintKaart:list, BingoKaart:list) -> list:
    Getallen = KrijgOverigeNummers(PrintKaart, BingoKaart)
    for i in range(3):
        Getallen.append("Roden bal")
        Getallen.append("Groenen bal")
    return Getallen
    


#Zet bingokaart om naar een string
def BingoKaartNaarString(Kaart:list) -> str:
    string = ''
    for rij in Kaart:
        for i in rij:
            string = string + str(i) + " "
        string = string + '\n'
    return string

#returned een lijst met alle nummer die nog niet getrokken zijn
def KrijgOverigeNummers(PrintKaart:list, BingoKaart:list) -> list:
    OverigeNummerss = []
    for rij in range(len(BingoKaart)):
        for i in range(len(BingoKaart[rij])):
            if PrintKaart[rij][i] == BingoKaart[rij][i]:
                OverigeNummerss.append(BingoKaart[rij][i])
    return OverigeNummerss

#Pak een bal
def PakEenBal(PrintKaart:list, BingoKaart:list, BallenBak:list) -> None:
    Bal = random.choice(BallenBak)
    BallenBak.remove(Bal)
    print(f"Je hebt {Bal} gepakt")

    for rij in range(len(BingoKaart)):
        for i in range(len(BingoKaart[rij])):
            if BingoKaart[rij][i] == Bal:
                PrintKaart[rij][i] = colored(PrintKaart[rij][i], "green")

    print("Je bingo kaart is nu:", "\n", BingoKaartNaarString(PrintKaart))
    
    return PrintKaart, BingoKaart, BallenBak

#Checkt of je 3 ballen hebt
def CheckBallen(Rood:int, Groen:int):
    if Rood == 3:
        print("Je Bent af je hebt 3 rode ballen gepakt")
        exit()
    if Groen == 3:
        print("Je Hebt gewonnen je hebt 3 groene ballen gepakt")
        exit()

#Pakt het aantal ballen dat je gepakt heb
def KrijgAantalBallen(BallenBak:list) -> list:
    #Aantal kleur ballen
    RodeBallen = 0-3
    GroeneBallen = 0-3
    for bal in BallenBak:
        if bal == "Roden bal":
            RodeBallen += 1
        if bal == "Groenen bal":
            GroeneBallen += 1
    return RodeBallen, GroeneBallen



def KijkVoorBingo(PrintKaart, BingoKaart) -> bool:
    #Horizontaal
    for Rij in range(4):
        IsBingo = True
        for Getal in range(4):
            if BingoKaart[Rij][Getal] == PrintKaart[Rij][Getal]:
                IsBingo = False
        if IsBingo == True:
            return IsBingo
    
    #Verticaal
    for Rij in range(4):
        IsBingo = True
        for Getal in range(4):
            if BingoKaart[Getal][Rij] == PrintKaart[Getal][Rij]:
                IsBingo = False
        if IsBingo == True:
            return IsBingo