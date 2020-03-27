#--------------- P G P dev -------------------------------------------------
"""
Release note
*   Present code allows to self move the mouse cursor from left to right
    at the upper left side of the screen.
*   User can modify the time between loop, looking into time.sleep
*   To terminate the process, press "Esc" key
"""

import pyautogui
import pynput
import time
import sys

pyautogui.FAILSAFE = True

from pynput.keyboard import Key, Listener 


def on_release(key):
    if key == Key.esc:                              # checks if esc key was pressed
        #print("funca")                             # print to check listener works
        return False                                # to kills listener 

if __name__ == '__main__':
    listener = Listener (on_release=on_release)
    listener.start()

    while True:
        pyautogui.moveTo(100, 100, duration=0.25)   # sets cursor at the upper left side of the screen
        pyautogui.moveTo(200, 100, duration=0.25)   # moves the cursor 100 px to the right
        time.sleep(3)                               # sets the time between movement loop

        if not listener.is_alive():                 # checks if listener is working
            break                                   # kills the while loop if esc was pressed 
           
 
#--------------- P G P dev -------------------------------------------------