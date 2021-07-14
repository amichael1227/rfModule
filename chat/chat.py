#!/usr/bin/env python3

# Import libraries we need
import time
import serial
import threading
import sys

# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)

# Creates the global variable needed for later
message = ''


# Function to get and decode the message
def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    message = x.decode()

def send(arg1):
    # Transmit your message
    print('Transmitting...')
    while 1:
        s = sys.stdin.readline()
        ser.write(s.encode())
        time.sleep(0.25)

def recieve(arg1):
    global message
    print('Recieving...')
    while 1:
        # Get the decoded message and format it
        readAndDecode()
        message = message.replace('\n', '')
        print(message)
        time.sleep(0.25)

try:
    # Create and start the threads
    sendThread = threading.Thread(name='getAndSave', target=send, args=(1,)).start()
    recieveThread = threading.Thread(name='action', target=recieve, args=(1,)).start()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("Exiting.")
    exit