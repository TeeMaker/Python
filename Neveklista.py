Vezetéknevek = []
Keresztnevek = []
i = 1

while i <= 5:
    Keresztnevek.append(input('Add meg a(z) ' + str(i) + '. vezetéknevet! '))
    Vezetéknevek.append(input('Add meg a(z) ' + str(i) + '. keresztnevet! '))
    i += 1
print(Vezetéknevek, '\n', Keresztnevek)
