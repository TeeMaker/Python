név = input("Mi a neved? ")
kor = input("Hány éves vagy? ")
jelenlegi_év = input("Milyen évet írunk? ")
jelenlegi_év = int(jelenlegi_év)
kor = int(kor)
születési_év = jelenlegi_év - kor
print(név, ",", születési_év, "-ben születtél.", sep="")
