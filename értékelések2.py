#!/usr/bin/python3

jegy = input("Adj meg egy számot 1 és 5 között! ")
jegy = int(jegy)


if jegy == 5 and jegy != 4 and jegy != 3 and jegy != 2 and jegy != 1:
    print(int(jegy), " jeles", sep= "")
if jegy != 5 and jegy == 4 and jegy != 3 and jegy != 2 and jegy != 1:
    print(int(jegy), " jó", sep= "")
if jegy != 5 and jegy != 4 and jegy == 3 and jegy != 2 and jegy != 1:
    print(int(jegy), " közepes", sep= "")
if jegy != 5 and jegy != 4 and jegy != 3 and jegy == 2 and jegy != 1:
    print(int(jegy), " elégséges", sep= "")
if jegy != 5 and jegy != 4 and jegy != 3 and jegy != 2 and jegy == 1:
    print(int(jegy), " elégtelen", sep= "")
