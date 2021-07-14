#!/usr/bin/env python3

# Import libraries we need
import time
import serial
import threading


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)

# Creates the global variable for the message we are getting
message = None
wasRead = False


def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
        message = x.decode()

# getAndSave thread
def getAndSave(arg1):
    global message
    while 1:
        readAndDecode()
        

# action thread
def action(arg1):
    global message
    global wasRead
    while 1:
        while (message != None and wasRead == False):
            print(message)
            wasRead = True


g = threading.Thread(name='getAndSave', target=getAndSave, args=(1,))
a = threading.Thread(name='action', target=action, args=(1,))



g.start()
a.start()