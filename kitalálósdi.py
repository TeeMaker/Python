#!/bin/python3

szám = 4
próbálkozások = 0
kitalálta = False

while not kitalálta and próbálkozások < 3:
    próbálkozások += 1
    tipp = input("Melyik számra gondoltam? ")
    tipp = float(tipp)
    if tipp == szám:
        kitalálta = True
        print("Ügyes vagy!")
    else:
        print("Ez nem sikerült!")

print("Szia!")
