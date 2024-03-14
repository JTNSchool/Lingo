from functies import *


Antwoord, SpelerWoord = MaakNieuwWoord()

while True:
    print(LijstNaarString(SpelerWoord))
    SpelerWoord = RaadWoord(Antwoord, SpelerWoord)
    
    if SpelerWoord == Antwoord:
        print('goed, volgende!')
        Antwoord, SpelerWoord = MaakNieuwWoord()

    
    