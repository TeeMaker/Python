#!/bin/python3

nap = ""
v = 0
def new_line():
    print("\n")

print("A hét napjai: ")

while v != 7:
    v += 1
    new_line()
    if v == 1:
        nap = "Hétfő"
    elif v == 2:
        nap = "Kedd"
    elif v == 3:
        nap = "Szerda"
    elif v == 4:
        nap = "Csütörtök"
    elif v == 5:
        nap = "Péntek"
    elif v == 6:
        nap = "Szombat"
    elif v == 7:
        nap = "Vasárnap"
    print(v, ". ", nap, sep="")
