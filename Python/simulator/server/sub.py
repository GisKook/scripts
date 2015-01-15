import zmq
import sys
sys.path.append("./pb")
import bcTx_pb2

port = "18889"

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://192.168.1.155:%s" % port)
socket.setsockopt(zmq.SUBSCRIBE, "")

while True:
    data = socket.recv()
    authfeedback = bcTx_pb2.BsfkMsg()
    authfeedback.ParseFromString(data[22:])
    print authfeedback.nAuthenticationId
    print authfeedback.sQtsentid
    print authfeedback.nRes

