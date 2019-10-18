sor = 0

while sor < 25:
    oszlop = 0
    while oszlop < sor + 1:
        print('÷×', end='')
        oszlop += 1
    print('')
    sor += 1
    if sor == 25:
        sor = 25
        while sor < 25:
            oszlop = 0
            while oszlop < sor:
                print('÷×', end='')
                oszlop += 1
        print('')
        sor -= 1
