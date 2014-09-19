__author__ = 'z'

import os
import sys
import subprocess
def ping(ip):
    subprocess.Popen("C:/Windows/System32/PING.EXE %s " % ip, shell=True, stdout=subprocess.PIPE)

def main():
    for i in range(1, 255):
        ip = "192.168.1."+str(i)
        print ip
        ping(ip)
        ip = "192.168.2."+str(i)
        print ip
        ping(ip)

if __name__ == "__main__":
    main()