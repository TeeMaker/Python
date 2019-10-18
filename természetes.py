szám = input('Adj meg egy számot! ')
szám = float(szám)
maradék = 0

if szám != 0:
    maradék = 1%szám

if szám >= 0 and maradék == 0:
    print('Ez a szám természetes!')
else:
    print('Ez a szám nem természetes!')
