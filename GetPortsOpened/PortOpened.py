#!/usr/bin/python
import sys
import socket

hostname = sys.argv[1]
port = 80

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = connect.connect_ex((hostname, port))

if result == 0:
    print "Open"
else:
    print "Close"
