#! /user/bin/python
# multiclient.py
import sys
import subprocess
import threading 

clientcount = sys.argv[1]
def execclient(index):
    conffile = file("./conf","r")
    line = conffile.readline()
    i = 0;
    while len(line) > 0:
        if i == index:
            conf = line.split(" ")
            command = ['python','./client.py', conf[0], conf[1][0:len(conf[1])-1]]
            print command
            subprocess.call(command)
        i = i+1
        line = conffile.readline()
    conffile.close()

def main():
    threads = []
    for i in range(int(clientcount)):  
        threads.append( threading.Thread(target=execclient,args=(i,)))  
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
