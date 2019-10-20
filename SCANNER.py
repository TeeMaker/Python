#!/usr/bin/python3

#Just importing
import sys
import socket
from datetime import datetime
import os

#Checking the arguments

if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1])
	beginning = sys.argv[2]
	beginning = int(beginning)
	end = sys.argv[3]
	end = int(end)
	end = end + 1
else:
	print('Invalid argument.')
	print('Syntax should be: python3 SCANNER.py <ip> <first_port> <last_port>')
	sys.exit()


#Making a banner

print('-' * 50)
print('Scanning host {}.'.format(target))
print('Time of start {}.'.format(str(datetime.now())))
print('-' * 50)

#Scanning the ports

try:
	for port in range(beginning,end + 1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Just to make it easier
		ports = []
		socket.setdefaulttimeout(1) #Set timout, float
		result = s.connect_ex((target, port))
		if result == 0:
			print('Port {} is open.'.format(port))
			ports.append(str(port))
			os.system('touch {}.txt'.format(target))
			os.system('echo port: {} is open >> {}.txt'.format(port, target))

#Error messages

except KeyboardInterrupt:
	print('Exiting program.')
	sys.exit()
except socket.gaierror:
	print('Could not resolve hostname.')
	sys.exit()
except socket.error:
	print('Could not connect to server.')
	sys.exit()