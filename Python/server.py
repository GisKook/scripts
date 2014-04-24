#!/bin/python

import sys
import socket


def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("127.0.0.1",5555))
	sock.listen(5)
	sockacc, addr=sock.accept()
	print "connect %s %d" % addr

	while True: 
		try:
			msg = sockacc.recv(1024)
			if len(msg) != 0:
				print msg
			sockacc.sendall(msg)
		except KeyboardInterrupt:
			break

if __name__=="__main__":
	main()
		
