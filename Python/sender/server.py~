import sys
import os
import socket
import string

ipaddr = sys.argv[1]
port = sys.argv[2]
recver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recver.bind((ipaddr, string.atoi(port)))

while True:
    content = recver.recv(1024)
    print content
