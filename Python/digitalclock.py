import time
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

while True:
	hour2 = 0
	while hour2 != 2:
		hour1 = 0
		while hour1 != 10:
			min2 = 0
			while min2 != 6:
				min1 = 0
				while min1 != 10:
					sec2 = 0
					while sec2 != 6:
						sec1 = 0
						while sec1 != 10:
							print(hour2,hour1,':',min2,min1,':',sec2,sec1)
							time.sleep(1)
							clear()
							sec1 += 1
						sec2 += 1
					min1 += 1
				min2 += 1
			hour1 += 1
		hour2 += 1
	hour2 = 2
	hour1 = 0
	while hour1 != 5:
		min2 = 0
		while min2 != 6:
			min1 = 0
			while min1 != 10:
				sec2 = 0
				while sec2 != 6:
					sec1 = 0
					while sec1 != 10:
						print(hour2,hour1,':',min2,min1,':',sec2,sec1)
						time.sleep(1)
						clear()
						sec1 += 1
					sec2 += 1
				min1 += 1
			min2 += 1
		hour1 += 1