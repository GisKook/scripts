#! /usr/bin/python
#push.py
import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:40001")
    bytes=[0,0,1]

    while True:
        socket.send_pyobj(bytes)
        time.sleep(1)

if __name__ == "__main__":
    main()
