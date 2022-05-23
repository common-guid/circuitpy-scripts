# SPDX-FileCopyrightText: 2021 jedgarpark for Adafruit Industries
# SPDX-License-Identifier: MIT

# Pico servo demo
# Hardware setup:
#   Servo on GP0 with external 5V power supply
#   Button on GP3 and ground
## CURCUIT PY
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

print("Servo test")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

def blink(times):
    for _ in range(times):
        led.value = False
        time.sleep(0.1)
        led.value = True
        time.sleep(0.1)

# Servo setup
pwm_servo = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 10, frequency=50)
servo1 = servo.Servo(
    pwm_servo, min_pulse=500, max_pulse=2200
)  # tune pulse for specific servo

## ^ Should be standard
servo1.angle = 90
time.sleep(2)'''
print("servo test: 180")
servo1.angle = 90
time.sleep(2)
print("servo test: 180")
servo1.angle = 180
time.sleep(2)
print("servo test: 180")
servo1.angle = 0'''