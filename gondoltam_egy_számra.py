gondolt_szám = 4
tipp = input('Melyik számra gondoltam, 1 és 5 között? ')
tipp = int(tipp)

if tipp > 5:
    print('Eszed nincsen!')
elif gondolt_szám == tipp:
    print('Eltaláltad!')
else:
    print('Sajnos nem találtad el!')
print('Szia!')
