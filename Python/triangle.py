import time
number = input('Mekkora haromszoget akarsz csinalni?(Szam)')
number = int(number)
v = 0
while v != 10:
	sor = 0
	while sor != number:
		oszlop = 0
		while oszlop != sor + 1:
			print(' ', end='')
			oszlop += 1
			time.sleep(0.1)
		print('O')
		sor += 1

	sor -= 1

	while sor != 1:
		oszlop = 0
		while oszlop != sor:
			print(' ', end='')
			oszlop += 1
			time.sleep(0.01)
		print('O')
		sor -= 1
	v += 1
