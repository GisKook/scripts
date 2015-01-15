#! /usr/bin/python
#simulator.py
import zmq
import sys
import struct
sys.path.append("./pb")
import bcTx_pb2
import smsTx_pb2

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://192.168.1.155:18888")
    socketpub = context.socket(zmq.PUB)
    socketpub.bind("tcp://*:18889")

    while True:
        data = socket.recv()
        bytes = bytearray(data)
        sendaddr = bytes[0:20]
        recvtype = bytes[20]
        recvaddr = bytes[21:41]
        messagelen = struct.unpack('< H', bytes[41:43])

        if recvtype == 1: # auth message
            auth = bcTx_pb2.BsTxMsg.FwjqMsg()
            auth.ParseFromString(data[43:])
            authfeedback = bcTx_pb2.BsfkMsg()
            authfeedback.nAuthenticationId = auth.nAuthenticationId
            authfeedback.sQtsentid = auth.sQtsentid
            authfeedback.nRes = 0
            strauthfeedback = authfeedback.SerializeToString() 
            format = '> 20sH%ds' % len(strauthfeedback)
            feedback = struct.pack(format, 'bill',len(strauthfeedback),strauthfeedback)
            socketpub.send(feedback)
            print 'ok you can post the message now.'
        elif recvtype == 2: # real message
            sendmessage = smsTx_pb2.BdfsMsg()
            sendmessage.ParseFromString(data[43:])
            sendmessagefeedback = smsTx_pb2.FsfkMsg()
            sendmessagefeedback.nSerialId = sendmessage.nSerialId
            sendmessagefeedback.nRes = 0 
            strsendmessagefeedback = sendmessagefeedback.SerializeToString()
            format = '> 20sH%ds' % len(strsendmessagefeedback)
            feedback = struct.pack(format, 'send', len(strsendmessagefeedback),strsendmessagefeedback)
            socketpub.send(feedback)
            print 'the message has been posted successfully.'
            
if __name__ == "__main__":
	main();
