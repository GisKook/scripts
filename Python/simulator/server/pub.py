#! /usr/bin/python
#simulator.py
from threading import Thread
import zmq
import random
import time

port = "30000"

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % port)

    while True:
        topic = random.randrange(10,20)
        print topic
        socket.send("%d" % topic)
        time.sleep(1)


if __name__ == "__main__":
	main();
