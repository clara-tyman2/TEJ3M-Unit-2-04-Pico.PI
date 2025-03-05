# Created by Clara T

# Created on Feb 2025

# Blink with Breadboard and LED with resistor

# Turns LED on for one second, the off for one second, each time increases each time by 1 more second


import time
import board
import digitalio

PIN_13 = digitalio.DigitalInOut(board.GP13)  # Red
PIN_13.direction = digitalio.Direction.OUTPUT

PIN_11 = digitalio.DigitalInOut(board.GP11) # Green
PIN_11.direction = digitalio.Direction.OUTPUT

PIN_12 = digitalio.DigitalInOut(board.GP12)  # Blue
PIN_12.direction = digitalio.Direction.OUTPUT


while True:
        # Green
        PIN_11.value = TRUE
        PIN_12.value = FALSE
        PIN_13.value = FALSE
        time.sleep(1)

        # Blue
        PIN_11.value = False
        PIN_12.value = TRUE
        PIN_13.value = FALSE
        time.sleep(1)

        # Red
        PIN_11.value = FALSE
        PIN_12.value = FALSE
        PIN_13.value = TRUE
        time.sleep(1)

        # Teal
        PIN_11.value = TRUE
        PIN_12.value = TRUE
        PIN_13.value = FALSE
        time.sleep(1)

        # Yellow
        PIN_11.value = TRUE
        PIN_12.value = FALSE
        PIN_13.value = TRUE
        time.sleep(1)

        # Purple
        PIN_11.value = FALSE
        PIN_12.value = TRUE
        PIN_13.value = TRUE
        time.sleep(1)

        # White
        PIN_11.value = TRUE
        PIN_12.value = TRUE
        PIN_13.value = TRUE
        time.sleep(1)
