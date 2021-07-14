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

# Background thread
def background(arg1):
    while 1:
        global message
        # Reads and decodes the message 
        x = ser.readline()
        # while (x.decode() == ''):
        #     x = ser.readline()
        message = x.decode()
        time.sleep(.1)
        

# Foreground thread
def foreground(arg1):
    while 1:
        global message
        # prints out the message when you press enter
        #input('Press Enter')
        while (message != None):
            print(message)
        time.sleep(.1)


b = threading.Thread(name='background', target=background, args=(1,))
f = threading.Thread(name='foreground', target=foreground, args=(1,))



b.start()
f.start()