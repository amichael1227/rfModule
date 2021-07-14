#!/usr/bin/env python3

# Import libraries we need
import time
import serial
import threading

from serial.serialutil import PARITY_NAMES


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


# Define the states
class State():
    IDLE = 0
    LED_ON = 1
    EMPTY = 2


# Creates the global variables needed later
message = ''
state = None


# Function to get and decode the message
def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    message = x.decode()


   
# Print messages
while 1:
    readAndDecode()
    print(message)