#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# initialise sensors and actuators
l_motor = Motor(Port.A)
r_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)

# color values for line detection. caliberate these for ever sensor.
BLACK = 5
WHITE = 553
threshold = (BLACK + WHITE) / 2

# drive speed and proportional gain for turning rate
DRIVE_SPEED = 400
PROPORTIONAL_GAIN = 2.5

# ================ UTILITY FUNCTIONS ================


def move_steer(speed, steer):
    # init l_speed and r_speed to same values
    l_speed = speed
    r_speed = speed

    gain = (50 - abs(float(steer))) / 50.0

    if steer >= 0:
        r_speed *= gain
    else:
        l_speed *= gain

    l_motor.run(l_speed)
    r_motor.run(r_speed)


# ==================== MAIN LOOP ====================
while True:
    # Calculate the deviation from the threshold.
    deviation = color_sensor.reflection() - threshold

    # Calculate the turn rate. e.g. 2.5 * 10 = 25 deg/s
    turn_rate = PROPORTIONAL_GAIN * deviation
    speed = DRIVE_SPEED

    move_steer(speed, turn_rate)
