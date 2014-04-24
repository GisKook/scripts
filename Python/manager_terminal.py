import random
import terminal
import string 
import time
import multiprocessing
import threading

terminal_process= []
terminal_threads= []
ipaddr = '127.0.0.1'
port = 8888

def manipulate_terminal():
	ter=terminal.terminal(str(random.randrange(100000000000000,999999999999999)),ipaddr, port)
	ter.login()
	while(not ter.flag):
		pass
	ter.flag=False
	ter.heartbeat()
	while(not ter.flag):
		pass

def multi_thread():
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
		for i in range(1000):
			terminal_process.append(multiprocessing.Process(target=multi_thread))
			terminal_process[i].start()

		for i in terminal_threads:
			i.join()
	except KeyboardInterrupt:
		pass

		
if __name__=="__main__":
	main()
