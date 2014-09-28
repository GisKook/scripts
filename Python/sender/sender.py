import sys
import socket
import random
import string
import time
from threading import Thread

# ipaddr = sys.argv[1]
# port = sys.argv[2]
ipaddr = "192.168.1.115"
port = "10000"
socket_count = 2000

imeis = []
file_content = file("E:/Code/scripts/Python/sender/imei.txt", "r")
def genimei():
    imei = file_content.readline()
    imeis.append(string.strip(imei, "\r\n"))
    return string.strip(imei, "\r\n")

sockets = []
socket_buf = []
def send_login(sockets_count):
    for i in range(sockets_count):
        imei = genimei()
        # print "$LOGIN:"+imei+":DK-PE100:DKP-PEV1.0\r\n"
        sockets[i].send("$LOGIN:"+imei+":DK-PE100:DKP-PEV1.0\r\n")

def create_socket(sockets_count):
    for i in range(sockets_count):
        sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

def connect_sockets(sockets_count):
    for i in range(sockets_count):
        sockets[i].connect((ipaddr, string.atoi(port)))

def send_heartbeat(socketindex, imei):
    sockets[socketindex].send("$HSTAT:"+imei+":0::99\r\n")
    # print "$HSTAT:"+imei+":0::99\r\n"

#for i in range(4):
#    thread = Thread(target=sendmsg)
#    thread.start()
#    thread.join()
#    thread.exit()
#     $POSUP:000000000036398:140928-095451:97:79:1:0:0:114.364204,38.057495
def send_position(socketindex, imei):
    curtime = time.localtime()
    year = str(curtime.tm_year - 2000)
    month = str(curtime.tm_mon)
    if len(month) == 1:
        month = "0"+month
    day = str(curtime.tm_mday)
    if len(day) == 1:
        day = "0"+day
    hour = str(curtime.tm_hour)
    if len(hour) == 1:
        hour = "0"+hour
    minute = str(curtime.tm_min)
    if len(minute) == 1:
        minute = "0"+minute
    second = str(curtime.tm_sec)
    if len(second) == 1:
        second = "0"+second

    timelabel = "{0}{1}{2}-{3}{4}{5}".format(year, month, day, hour, minute, second)
    # print "$POSUP:"+imei+":"+timelabel+":97:78:1:0:0:114.364204,38.057495\r\n"

    sockets[socketindex].send("$POSUP:"+imei+":"+timelabel+":97:78:1:0:0:114.364204,38.057495\r\n")

def thread_reportposition():
    first_reportposition = 1
    while True:
        if first_reportposition == 1:
            time.sleep(10)
            first_reportposition = 2
        time.sleep(5)
        for i in range(0,socket_count):
            send_position(i, imeis[i])

create_socket(socket_count)
connect_sockets(socket_count)
send_login(socket_count)

for i in range(0,socket_count):
    socket_buf.append("")
time.sleep(1)
thread = Thread(target = thread_reportposition)

thread.start()

while True:
    for i in range(0,socket_count):
        socket_buf[i] = sockets[i].recv(128)
        start = socket_buf[i].find('$')
        end = socket_buf[i].find('\r\n')
        if end != -1:
            buf = socket_buf[i][start:end]
            socket_buf[i] = socket_buf[i][end:]
            if len(buf) > 25:
                if buf.find("$LOGRT") != -1:
                    print buf
                    # if buf[24] == '1':
                    #     print buf.strip("$LOGRT").strip("::1\r\n") + " login sucess"
                    # else:
                    #     print buf.strip("$LOGRT").strip("::0\r\n") + " login error"
                if buf.find("$HCHECK") != -1:
                    send_heartbeat(i, buf[8:23])
                if buf.find("POSP") != -1:
                    print buf[6:21] + "recv position reply"

time.sleep(2)
print time.clock()-starttime
