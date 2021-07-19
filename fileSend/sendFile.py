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
from sys import stdin
import serial
from xmodem import XMODEM, CRC
from time import sleep
import os
from io import StringIO


# Sets up the file path for later 
outgoingPath = os.path.dirname(os.path.abspath(__file__)) + '/Outgoing/'
print ("Please make sure that the file is in the Outgoing folder!")
fileName = stdin("File name with extension: ")
outgoingPath = outgoingPath + fileName.replace('\n', '').replace(' ', '')


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
      ser.write(fileName.encode())


def readUntil(char = None):
    def serialPortReader():
        while True:
            tmp = ser.read(1)
            if not tmp or (char and char == tmp):
                break
            yield tmp
    return ''.join(serialPortReader())

def getc(size, timeout=1):
    return ser.read(size)

def putc(data, timeout=1):
    ser.write(data)
    sleep(0.001)


# Define the modem
modem = XMODEM(getc, putc)


# Reads and sends the file
sendFileName()
file = open(outgoingPath, 'rb')
modem.send(file)
readUntil()
print("File sent!")
