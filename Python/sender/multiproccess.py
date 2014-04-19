import subprocess
import thread
import os
import sys
import time
import string

process_count = string.atoi(sys.argv[3])
ipaddr = sys.argv[1]
port = sys.argv[2]

timestart=time.clock()

for i in range(process_count):
    subprocess.call(["C:\Python26\python.exe","C:\Users\Gis_Kook\PycharmProjects\untitled\sender.py",ipaddr,port])


print time.clock()-timestart
