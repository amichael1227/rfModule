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
    global message
    while 1:
        # Reads and decodes the message 
        x = ser.readline()
        while (x.decode() == ''):
             x = ser.readline()
        message = x.decode()
        time.sleep(.1)
        

# Foreground thread
def foreground(arg1):
    global message
    wasRead = False
    while 1:

        while (message != None and wasRead == False):
            print(message)
            wasRead = True
        time.sleep(.1)


b = threading.Thread(name='background', target=background, args=(1,))
f = threading.Thread(name='foreground', target=foreground, args=(1,))



b.start()
f.start()