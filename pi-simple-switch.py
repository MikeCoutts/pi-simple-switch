# Copyright The Kavinjka Software Company 2021
#
# Authour MikeC@kavinjka.com

import RPi.GPIO as GPIO
import time # for sleep functions

from signal import signal, SIGINT # for Cntrl-C
from sys import exit
from datetime import datetime

# Initialize the  GPIO Infrastructure to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Define Button GPIO port as an Input and define the previous_input variable
BUTTON = 16
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 (button) to be an input pin and set initial value to be pulled low (off)
previous_input = False

# Define an exit handler for the program (called on Cntrl-C)
def CntrlCHandler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    GPIO.cleanup()
    exit(0)

# setup  the Cntrl-C handler
signal(SIGINT, CntrlCHandler)

# infinite loop for the main thread (Use Cntrl-C to exit)
while True:
  # take a reading from the switch
  input = GPIO.input(BUTTON)

  # if the last reading was high and this one is low, signal Button Released
  if ((previous_input) and not input):
    currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Button Released at", currentDateTime)

  # update prev_input value 
  previous_input = input
 
  #slight pause to debounce
  time.sleep(0.05)
