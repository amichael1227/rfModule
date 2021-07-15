#!/usr/bin/env python3
# File Name:
# fileRecieve.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 15, 2021
# Decription:
# This program allows for files to be recieved over UART.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import serial
from xmodem import XMODEM
import time
import os


# Sets up the serial port for the RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)

# Sets up the file path for later 
incomingPath = os.path.dirname(os.path.abspath(__file__)) + '/Incoming/'
fileName = ''

# Function to get and decode the fileName
def readAndDecode():
    global fileName
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    fileName = x.decode()


# Function to recieve the file name
def getFileName():
    global fileName
    readAndDecode()
    fileName = fileName.replace('\n', '')
    print(fileName)
    time.sleep(1)


# Defines the function for getting a file
def getc(size, timout = 1):
  return ser.read(size) or None


# Defines the function for sending a file 
def putc(data, timeout = 1):
  return ser.write(data)


# Define the modem
modem = XMODEM(getc, putc)


# Gets and saves the file
getFileName()
stream = open('output.txt', 'wb')
modem.recv(stream)