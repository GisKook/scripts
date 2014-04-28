#!/bin/python
import socket
import string
import random
import time
import threading
import sys

class terminal:
	___imei=''
	__ipaddr=''
	__port=0
	__batt=0
	__sock=0
	__tread=0
	flag=False
	
	def __init__(self, imei, ipaddr, port):
		self.__imei=imei
		self.__ipaddr=ipaddr
		self.__port=port
		self.__sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__sock.setblocking(1)
		self.__thread=threading.Thread(target=self.__recvmsg__)
		self.__thread.start()
		self.__boot__()
				
	def __boot__(self):
		self.__batt=random.randrange(0, 100)
		try:
			self.__sock.connect((self.__ipaddr, self.__port))
		except socket.error:
			print "connect to server.... fail!"

	def __recvmsg__(self):
		while True:
			try:
				time.sleep(1)
				msg = self.__sock.recv(1024)
				self.flag=True
				if len(msg)!=0:
					print msg
			except KeyboardInterrupt:
				break

	def login(self):
                try:
                    self.__sock.send("$LOGIN:"+self.__imei+":DK-PE100:DKP-PEV1.0\r\n") 
                    time.sleep(0.5)
                except KeyboardInterrupt:
                    sys.exit()

	def heartbeat(self):
		self.__sock.send("$HSTAT:"+self.__imei+"::"+str(self.__batt)+"\r\n")
		time.sleep(0.5)

def main():
	ter=terminal("1111", "127.0.0.1", 5005)
	while True:
            ter.login()
if __name__=="__main__":
	main()
