
import zmq
import random
import sys
import time

# pairserver.py

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
time.sleep(1)

while True:
    print "Server Waiting..."
    msg = socket.recv()
    print msg
    socket.send("Hello from server")

 