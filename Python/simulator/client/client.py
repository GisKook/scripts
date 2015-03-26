#! /usr/bin/python
# client.py

import socket
import struct
import sys
from threading import Thread
from threading import Event
import time
import binascii

if len(sys.argv) < 4:
    print '''
        need login ,password, cardid
        usage:
            client.py login password cardid
    '''
    exit()

login = sys.argv[1]
password = sys.argv[2]
cardid = sys.argv[3]
ipaddr="192.168.1.155"
port = 30000

def calcchecksum(bytes): 
    length = len(bytes)
    result = bytes[0]
    for i in range(1,length): 
        result ^= bytes[i]

    return result

def loginfunc(sock,login, password):
    format = "> 5sH12s8s"
    bytes = bytearray(struct.pack(format, "$YHZC", 28, login, password))
    sum = calcchecksum(bytes)
    bytes.append(sum)
    sock.send(bytes)

def heartbeat(sock, login):
    format = "> 5sH12s"
    bytes = bytearray(struct.pack(format, "$XTJC", 20, login))
    sum = calcchecksum(bytes)
    bytes.append(sum)
    sock.send(bytes)

def reqfunc(sock, index):
    format = "> 5sHIIIBH5s"
    bytes = bytearray(struct.pack(format, "$BDFS", 28,index, int(cardid), 0, 1,5,"cetcn"))
    sum = calcchecksum(bytes)
    bytes.append(sum)
    sys.stdout.write(cardid)
    sys.stdout.write("send request ")
    print "send request"
    sock.send(bytes) 

def recvmsg(sock,event):
    while True:
        message = sock.recv(256)
        if message.find("$DWXX") != -1:
            print "%s find position message." % login
        elif message.find("$XTYD") != -1:
            print "%s recv heart beat." % login
        elif message.find("$FSFK") != -1:
            print "%s recv feedback message." % login
        else:
            sys.stdout.write(".........")
            print binascii.hexlify(message)

        if message[0:5] == "$ZCFH":
            result = struct.unpack('B', message[19])
            result = int(result[0])
            if result == 0 :
                print "login success."
                event.set()
            elif result == 1:
                print "password error."
                return 1
            elif result == 2:
                print "no user."
                return 2
            elif result == 3:
                print "already login."
                return 3
            else:
                print "recv a error login feedback message."
                return 4
#        elif message[0:5] == "$XTYD":
#           print " recv heart beat" 
#        elif message[0:5] == "$FSFK":
#            print "recv feedback message"
#        elif message[0:5] == "$DWXX":
#            print "recv position message"
#        else:
#            sys.stdout.write("..............")
#            print binascii.hexlify(message)

        time.sleep(1)

def heart(sock,login):
    while True: 
        heartbeat(sock, login)
        time.sleep(20)

def req(sock):
    index = 0
    while True:
        reqfunc(sock, index)
        index = index+1
        time.sleep(1)
        
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    rc = sock.connect_ex((ipaddr, port))
    if rc != 0:
        print "connect error %s %d" %(ipaddr ,port)
        exit()

    event = Event()
    threadrecv= Thread(target=recvmsg, args=(sock,event))
    threadrecv.start() 
    loginfunc(sock, login, password)

    loginresult = event.wait(20)
    if loginresult == True:
        threadheart = Thread(target=heart, args=(sock, login))
        threadheart.start()
        threadreq = Thread(target=req, args=(sock,))
        threadreq.start()
        threadheart.join()
        threadreq.join()

    threadrecv.join()

if __name__ == "__main__":
    main()
