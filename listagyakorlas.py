import os

előadók= []
v = 1
előadó = None
számok = []
szám = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print('Ez a program az öt kedvenc zenei előadódat és számaikat fogja tőled megkérdezni és külön listákban tárolni.')

while v != 6:
    előadó = input('Add meg a(z) {}. kedvenc előadódat! '.format(v))
    szám = input('Most adj meg a kedvenc számodat az előbbi előadótól: ')
    if előadó and szám:
        előadók.append(előadó)
        számok.append(szám)
        v += 1
        clear()
    else:
        print('Nem helyes adatokat adtál meg')
print(előadók)
print(számok)
kombinált = []
kombinált = list(zip(előadók, számok))
print(kombinált)
