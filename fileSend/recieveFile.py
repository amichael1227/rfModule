#!/usr/bin/env python3
# File Name:
# fileRecieve.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 19, 2021
# Decription:
# This program allows for files to be recieved over UART. Currently appends a bunch of '^Z's to the file though.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import serial
from xmodem import XMODEM
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
incomingPath = str(os.path.dirname(os.path.abspath(__file__))) + '/Incoming/'


# Function to get and decode the fileName
def readAndDecode():
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    fileName = x.decode()
    return fileName


# Function to recieve the file name
def getFileName():
    fileName = readAndDecode()
    fileName = incomingPath + fileName.replace('\n', '')
    return fileName


# Defines the function for getting a file
def getc(size, timeout = 1):
  return ser.read(size) or None


# Defines the function for sending a file 
def putc(data, timeout = 1):
  return ser.write(data)


# Define the modem
modem = XMODEM(getc, putc)


# Gets and saves the file
fileName = getFileName()
file = open(fileName, 'wb')
modem.recv(file)
with open(fileName, 'r') as infile, \
     open(fileName, 'w') as outfile:
    data = infile.read()
    data = data.replace('^Z', '')
    outfile.write(data)
print("File recieved!")