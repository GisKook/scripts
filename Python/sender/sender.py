import sys
import socket
import random
import string
import time
from threading import Thread

ipaddr = sys.argv[1]
port = sys.argv[2]

def genimei():
    return random.randrange(100000000000000,999999999999999)

sockets  =[]
def send_msg(sockets_count):
    for i in range(sockets_count):
        sockets[i].send("$LOGIN:"+str(genimei())+":DK-PE100:DKP-PEV1.0\r\n")
        time.sleep(1)


def create_socket(sockets_count):
    for i in range(sockets_count):
        sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

def connect_sockets(sockets_count):
    for i in range(sockets_count):
        print "connect "
        sockets[i].connect((ipaddr, string.atoi(port)))

starttime=time.clock()
#for i in range(4):
#    thread = Thread(target=sendmsg)
#    thread.start()
#    thread.join()
#    thread.exit()
create_socket(400)
connect_sockets(400)
send_msg(400)
time.sleep(2)
print time.clock()-starttime
