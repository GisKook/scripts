#! /user/bin/python
# multiclient.py
import sys
import subprocess
import threading 

if len(sys.argv) < 3:
    print '''
    need a client count, beiginindex
    python multiclient.py clientcount clientbeginindex
    '''
    exit()

clientcount = sys.argv[1]
clientbeginindex = sys.argv[2]

def execclient(index):
    conffile = file("./conf","r")
    line = conffile.readline()
    i = 0;
    while len(line) > 0:
        if i == index:
            conf = line.split(" ")
            command = ['python','./client.py', conf[0], conf[1],conf[2][0:len(conf[2])-1]]
            print command
            subprocess.call(command)
        i = i+1
        line = conffile.readline()
    conffile.close()

def main():
    threads = []
    for i in range(int(clientcount)):  
        threads.append( threading.Thread(target=execclient,args=(i+int(clientbeginindex),)))  
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
