#!/usr/bin/env python3
# File Name:
# recieve.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# Alexander Corey
# ajcorey@wpi.edu
# July 14, 2021
# Decription:
# This program recieves messages over UART and prints out what that message says.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE


# Import libraries this program need
import time
import serial
import threading

from serial.serialutil import PARITY_NAMES


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


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