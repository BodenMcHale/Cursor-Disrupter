# To move the cursor
import pyautogui
# For sleep intervals
import time
# CLI arguments
import argparse
import sys
# Info on cursor movements
from datetime import datetime

import cursordisrupter

# Prevent PyAutoGUI from triggering the failsafe
pyautogui.FAILSAFE = False

# Intervals between cursor movements and key presses
interval_count = 1

def main(argv=None):
    while True:
        current_interval = 0
        # Wait for one minute per interval
        while current_interval < interval_count:
            # Wait one minute
            time.sleep(60)
            # Increment the interval
            current_interval += 1

        # Move the cursor
        for i in range(0, 100):
            pyautogui.moveTo(0, 0)
            pyautogui.moveTo(0, i * 5)

        # Retrieve the current time
        current_time = datetime.now()
        # Format the time
        date_time_string = current_time.strftime("%H:%M:%S")
        # Display the current timestamp
        print ("Cursor Disrupted Timestamp: " + date_time_string)