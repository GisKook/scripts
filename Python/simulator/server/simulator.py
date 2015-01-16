#! /usr/bin/python
#simulator.py
import zmq
import datetime
from threading import Thread
import sys
import struct
import random
import time
sys.path.append("./pb")
import bcTx_pb2
import smsTx_pb2
import beidoumessage_pb2


def beidoumessagepositioninfo(sock):
    beidoumessage = beidoumessage_pb2.Beidoumessage()
    beidoumessage.messagetype = 0
    beidoumessage.positioninfo.userid = 310732
    beidoumessage.positioninfo.encryption = 0
    beidoumessage.positioninfo.accuracy = 0
    beidoumessage.positioninfo.emergencypostion = 0
    beidoumessage.positioninfo.multivaluesolution = 0
    beidoumessage.positioninfo.key = ''
    currenttime = datetime.datetime.now()
    beidoumessage.positioninfo.applytime_hour = currenttime.hour
    beidoumessage.positioninfo.applytime_minute = currenttime.minute
    beidoumessage.positioninfo.applytime_second = currenttime.second
    beidoumessage.positioninfo.applytime_tenths = int(round(currenttime.microsecond/10))
    beidoumessage.positioninfo.longitude_degree = 138
    beidoumessage.positioninfo.longitude_minute = 43
    beidoumessage.positioninfo.longitude_second = 24
    beidoumessage.positioninfo.longitude_tenths = 7
    beidoumessage.positioninfo.latitude_degree = 77
    beidoumessage.positioninfo.latitude_minute = 58
    beidoumessage.positioninfo.latitude_second = 52
    beidoumessage.positioninfo.latitude_tenths = 1
    beidoumessage.positioninfo.geodeticheight = 54
    beidoumessage.positioninfo.detlaelevation = -23
    strpositioninfo = beidoumessage.SerializeToString() 
    format = '> 20sH%ds' % len(strpositioninfo)
    bytearraypositioninfo = struct.pack(format, 'recv', len(strpositioninfo), strpositioninfo)
    sock.send(bytearraypositioninfo)
    print "send a position info"

def beidoumessagecommunication(sock):
    beidoumessage = beidoumessage_pb2.Beidoumessage()
    beidoumessage.messagetype = 3
    beidoumessage.communication.messageform = 0
    beidoumessage.communication.messagecategory = 0
    beidoumessage.communication.encryption = 0
    beidoumessage.communication.sendaddr = 310732
    beidoumessage.communication.recvaddr = 524039
    currenttime = datetime.datetime.now()
    beidoumessage.communication.sendtime_hour = currenttime.hour
    beidoumessage.communication.sendtime_minute = currenttime.minute
    beidoumessage.communication.sendtime_second = currenttime.second
    beidoumessage.communication.key = ''
    beidoumessage.communication.messagelength = 7
    beidoumessage.communication.messagebuffer = "cetcnav"
    strcommunication = beidoumessage.SerializeToString()
    format = '> 20sH%ds' % len(strcommunication)
    bytearraycommunication = struct.pack(format, 'recv', len(strcommunication), strcommunication)
    sock.send(bytearraycommunication)

    print "send a communication info"

def beidoumessagecommunicationreceipt(sock):
    beidoumessage = beidoumessage_pb2.Beidoumessage()
    beidoumessage.messagetype = 4
    beidoumessage.communicationreceipt = beidoumessage_pb2.Communicationreceipt()
    beidoumessage.communicationreceipt.sendaddr = 310732
    beidoumessage.communicationreceipt.recvaddr = 524039
    currenttime = datetime.datetime.now()
    beidoumessage.communicationreceipt.receipttime_hour = currenttime.hour
    beidoumessage.communicationreceipt.receipttime_minute = currenttime.minute
    beidoumessage.communicationreceipt.receipttime_second = currenttime.second
    strcommunicationreceipt = beidoumessage.SerializeToString()
    format = '> 20sH%ds' % len(strcommunicationreceipt)
    bytearraycommunicationreceipt = struct.pack(format, 'recv', len(strcommunicationreceipt), strcommunicationreceipt)
    sock.send(bytearraycommunicationreceipt)
    print "send a communicationreceipt info"

def beidoumessagerecvier(sock):
    while True:
        beidoumessagepositioninfo(sock)
#        beidoumessagecommunication(sock)
#        beidoumessagecommunicationreceipt(sock)
        time.sleep(1)

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://192.168.1.155:18888")
    socketpub = context.socket(zmq.PUB)
    socketpub.bind("tcp://*:18889")
    threadbeidourecv = Thread(target=beidoumessagerecvier, args=(socketpub,))
    threadbeidourecv.start() 
    threadbeidourecv.deamon = True

    while True:
        data = socket.recv()
        bytes = bytearray(data)
        sendaddr = bytes[0:20]
        recvtype = bytes[20]
        recvaddr = bytes[21:41]
        messagelen = struct.unpack('< H', bytes[41:43])

        if recvtype == 1: # auth message
            message = bcTx_pb2.BsTxMsg()
            message.ParseFromString(data[43:])
            if message.nRecvType == bcTx_pb2.BsTxMsg.FWJQ:
                authfeedback = bcTx_pb2.BsfkMsg()
                authfeedback.nAuthenticationId = message.fwjqMsg.nAuthenticationId
                authfeedback.sQtsentid = message.fwjqMsg.sQtsentid
                authfeedback.nRes = 0
                strauthfeedback = authfeedback.SerializeToString() 
                format = '> 20sH%ds' % len(strauthfeedback)
                feedback = struct.pack(format, 'bill',len(strauthfeedback),strauthfeedback)
                socketpub.send(feedback)
                print 'ok you can post the message now.'
            elif message.nRecvType == bcTx_pb2.BsTxMsg.KFQQ:
                print 'charge it !!!!'

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
