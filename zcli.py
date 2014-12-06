
import zmq
import random
import sys
import time

# pairclient.py

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.01:%s" % port)

while True:
	print "Sending"
	socket.send("Hello from client")
	msg = socket.recv()
	print msg
	time.sleep(1)