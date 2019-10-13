def quad():

	# from math import sqrt
	#from math import *
	# x ** 0.5
	from math import sqrt
	print('This program will find the root of a quadratic equation')
	print('Input values as the following: a * x ** 2 + b * x + c!')
	a = float(input('Please input a: '))
	b = float(input('Please input b: '))
	c = float(input('Please input c: '))
	print()
	disc = b ** 2 - 4 * a * c
	if disc >=0:
		disc1 = sqrt(disc)
		positive = (-b + disc1) / (2 * a)
		negative = (-b - disc1) / (2 * a)
		print(positive, negative)
	else:
		print('There is no root!')	

start = input('Input something to start the program, leave empty to exit! ')

while start != '':
	quad()
	start = input('Input something to start the program, leave empty to exit! ')