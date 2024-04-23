from Data import *
import random
from termcolor import colored
import os

#Genereerd een nieuw woord dat geraden moet worden
def MaakNieuwWoord():
    Antwoord = random.choice(WORDS)
    SpelerWoord = []
    for i in range(len(Antwoord)):
        SpelerWoord.append("_")
    VorigeWoorden = [SpelerWoord.copy()]
    VorigeWoorden[0][0] = Antwoord[0]

    print(Antwoord)

    return Antwoord, SpelerWoord, VorigeWoorden

#Vraag om een input
def RaadWoord(Antwoord:str) -> list:
    while True:
        Woord = input(f"vul een woord in van {len(Antwoord)} letters:\n").lower()
        if len(Woord) == len(Antwoord) and Woord.isalpha():
            #Afstreep lijsten
            TijdelijkAntwoord = list(Antwoord)
            TijdelijkWoord = list(Woord)
            ReturnWoord = []
            for i in Woord:
                ReturnWoord.append(i)
            #Groen
            for i in range(len(Antwoord)):
                if TijdelijkWoord[i] == TijdelijkAntwoord[i]:
                    ReturnWoord[i] = colored(TijdelijkWoord[i], "green")
                    TijdelijkWoord[i] = "_"
                    TijdelijkAntwoord[i] = "_"
                    
            #Geel
            for i in range(len(TijdelijkWoord)):
                if TijdelijkWoord[i] in TijdelijkAntwoord and TijdelijkWoord[i] != "_":
                    ReturnWoord[i] = colored(TijdelijkWoord[i], "yellow")
                    TijdelijkWoord[i] = "_"
                    for i in range(len(TijdelijkAntwoord)):
                        if TijdelijkAntwoord[i] == TijdelijkWoord[i]:
                            TijdelijkAntwoord[i] = "_"
            
            return ReturnWoord, Woord
        else:
            print(colored(f"het woord moet {len(Antwoord)} letters hebben!", "red"))

#Laat het scherm zien
def Scherm(Word:str, PrintWoord:list, VorigeWoorden:list):
    #os.system('cls' if os.name == 'nt' else 'clear')
    for woord in VorigeWoorden:
        print(LijstNaarString(woord))
    


#een woord die in een lijst staat omzetten naar string
def LijstNaarString(lijst:list) -> str:
    string = ""
    for letter in lijst:
        string = string + letter 
    return string