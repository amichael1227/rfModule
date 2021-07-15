#!/usr/bin/env python3
# File Name:
# chatGUI.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 14, 2021
# Decription:
# This program allows for messages to be sent back and forth over UART.
# Very similar to chat.py, but has a nice GUI.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import time
import serial
import threading
import sys
from tkinter import * 

# Sets up the serial port for our RF Modules
# ser = serial.Serial(
#   port = "/dev/ttyS0",
#   baudrate = 9600,
#   parity = serial.PARITY_NONE,
#   stopbits = serial.STOPBITS_ONE,
#   bytesize = serial.EIGHTBITS,
#   timeout = 1
# )

# Creates the global variable needed for later
#recievedMessage = ''
#sentMessage = ''


# Creates the Tkinter things we need for our chatbox
window = Tk()
messageHistory = Text(window)
messageHistory.pack()
userInput = StringVar()
inputField = Entry(window, text = userInput)
inputField.pack(side = BOTTOM, fill = X)

# # Function to get and decode the recieved message
# def readAndDecode():
#     global recievedMessage
#     x = ser.readline()
#     while (x.decode() == ''):
#         x = ser.readline()
#     recievedMessage = x.decode()

# Function that triggers sending message
def enterPressed(event):
    global message
    getInput = inputField.get()
    messageHistory.insert(INSERT, '%s\n' % getInput)
    message = getInput
    userInput.set('')
    return "break"

# # Function to transmit the message
# def transmit(arg1):
#     print("Transmitting...")
#     while 1:
#         s = sys.stdin.readline()
#         ser.write(s.encode())
#         time.sleep(0.25)

# # Function to recieve the message
# def recieve(arg1):
#     global message
#     print("Recieving... \n")
#     while 1:
#         # Get the decoded message and format it
#         readAndDecode()
#         message = message.replace('\n', '')
#         print(message)
#         time.sleep(0.25)


# Try loop to allow for graceful exit
try:
    # Create and start the threads that allow the devices to chat
    transmitThread = threading.Thread(name="sending", target=transmit, args=(1,)).start()
    recieveThread = threading.Thread(name="recieving", target=recieve, args=(1,)).start()
    # Continuously updates the Tkinter GUI screen
    frame = Frame(window)
    inputField.bind("<Return>", enterPressed)
    frame.pack()
    window.mainloop()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    sys.exit("Program exiting!")



