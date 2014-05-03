import random
import terminal
import string 
import time
import multiprocessing
import threading

terminal_process= []
terminal_threads= []
ipaddr = '127.0.0.1'
port = 5005 

def multi_process():
    print "******"
    ter=terminal.terminal(str(random.randrange(100000000000000,999999999999999)),ipaddr, port)
    ter.login()
    print "ssssssss*****"
    ter.flag=False
    while True:
        ter.heartbeat()
        time.sleep(0.5)

def multi_proces_t():
    try:
        for i in range(10):
            terminal_threads.append(threading.Thread(target=manipulate_terminal))
            terminal_threads[i].start()
        for i in terminal_threads:
            i.join()

    except KeyboardInterrupt:
        pass

def main():
    try:
        for i in range(2):
            p= multiprocessing.Process(target=multi_process)
            p.start()
            terminal_process.append(p)

        for p in terminal_process:
            p.join

    except KeyboardInterrupt:
        pass


if __name__=="__main__":
    main()
