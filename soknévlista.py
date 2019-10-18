Vezetéknevek = []
Keresztnevek = []
Vezetéknév = None

while Vezetéknév != '':
    Vezetéknév = input('Adj meg egy vezetéknevet! ')
    Keresztnév = input('Most pedig a hozzá tartozó keresztnevet! ')
    if Vezetéknév and Keresztnév:
        Vezetéknevek.append(Vezetéknév)
        Keresztnevek.append(Keresztnév)
    elif not Keresztnév:
        print('Nem érvényes név, próbáld újra!')
print(Vezetéknevek, '\n', Keresztnevek)
