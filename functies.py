from Data import *
import random
from termcolor import colored

#Creer een team en vraagt namen
def CreerTeam() -> list:
    Team = []
    for i in range(1, TEAMAANTAL+1):
        persoon = input(f"Wat is de naam van teamlid {i}? ")
        #Check double in list
        Team.append(persoon)
    return Team

#Genereerd een nieuw woord dat geraden moet worden
def MaakNieuwWoord():
    Antwoord = random.choice(WORDS)
    SpelerWoord = [Antwoord[0]]
    for i in range(len(Antwoord)-1):
        SpelerWoord.append("_")
    return Antwoord, SpelerWoord

#Vraag om een input
def RaadWoord(Antwoord:str, SpelerWoord:list) -> list:
    while True:
        Woord = input(f"vul een woord in van {len(Antwoord)} characters:\n")
        if len(Woord) == len(Antwoord):
            #Afstreep lijsten
            TijdelijkAntwoord = list(Antwoord)
            TijdelijkWoord = list(Woord)
            #Groen
            for i in range(len(Antwoord)):
                if TijdelijkWoord[i] == TijdelijkAntwoord[i]:
                    SpelerWoord[i] = colored(TijdelijkWoord[i], "green")
                    
            #Geel
            for i in range(len(TijdelijkWoord)):
                if TijdelijkWoord[i] in TijdelijkAntwoord:
                    if SpelerWoord[i] != colored(TijdelijkAntwoord[i], 'green'):
                        SpelerWoord[i] = colored(TijdelijkWoord[i], "yellow")
            
            return SpelerWoord
        else:
            print(colored(f"het woord moet {len(Antwoord)} characters hebben!", "red"))

#een woord die in een lijst staat omzetten naar string
def LijstNaarString(lijst:list) -> str:
    string = ""
    for letter in lijst:
        string = string + letter 
    return string