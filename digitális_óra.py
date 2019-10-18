másodperc1 = 0
másodperc2 = 0
perc2 = 0
óra2 = 0

while óra2 != 3:
    óra1 = 0
    while óra1 != 9:
        perc2 = 0
        while perc2 != 6:
            perc1 = 0
            while perc1 != 10:
                másodperc2 = 0
                while másodperc2 != 6:
                    másodperc1 = 0
                    while másodperc1 != 10:
                        print(óra2, óra1, ':', perc2, perc1, ':', másodperc2, másodperc1, sep='')
                        másodperc1 += 1
                    másodperc2 +=1
                perc1 += 1
            perc2 += 1
        óra1 += 1
    óra2 += 1
    
