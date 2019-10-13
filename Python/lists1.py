import os

def clear():
		os.system('cls' if os.name =='nt' else 'clear')
heroes = []
 
hero = None
 
while hero != '':
	hero = input('Name a hero! ')
	if hero: 
		heroes.append(hero)
	clear()
print(heroes)