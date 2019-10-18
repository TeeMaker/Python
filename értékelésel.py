#!/usr/bin/python3
#1-5ög számok mellé az elnevezése a jegynek, elifes

jegy = input("Adj meg 1től 5ig egy számot! ")
jegy = float(jegy)

if jegy == 1:
    print(int(jegy), " elégtelen")
elif jegy == 2:
    print(int(jegy), " elégséges")
elif jegy == 3:
    print(int(jegy), " közepes")
elif jegy == 4:
    print(int(jegy), " jó")
elif jegy == 5:
    print(int(jegy), " jeles")
else:
    print("Nem jó számot adtál meg!")

print("A programnak vége, hello!")
