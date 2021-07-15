#!/usr/bin/env python3
# File Name:
# fileSend.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 15, 2021
# Decription:
# This program allows for files to be sent over UART.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import serial
from xmodem import XMODEM
import os
import time
import sys


# Sets up the file path for later 
outgoingPath = os.path.dirname(os.path.abspath(__file__)) + '/Outgoing/'
print ("Please make sure that the file is in the Outgoing folder!")
fileName = input("File name with extension: '")


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


# Function to transmit the message
def sendFileName():
    while 1:
        ser.write(fileName.encode())
        time.sleep(1)


# Defines the function for getting a file
def getc(size, timout = 1):
  return ser.read(size) or None


# Defines the function for sending a file 
def putc(data, timeout = 1):
  return ser.write(data)


# Define the modem
modem = XMODEM(getc, putc)


# Reads and sends the file
sendFileName()
modem.send(open(fileName, 'rb'))