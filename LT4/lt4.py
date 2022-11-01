#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math

def straight():
    left_motor.run(speed)
    right_motor.run(speed)
    value = gyro_sensor.angle()
    if (value < 0):
        right_motor.run(speed + (value * drift))
    elif (value > 0):
        left_motor.run(speed - (value * drift))

def dash():
    left_motor.hold()
    right_motor.hold()
    left_motor.reset_angle(0)
    left_motor.run(dashSpeed)
    right_motor.run(dashSpeed)
    while(True):
        if (left_motor.angle() > dashDistance):
            left_motor.hold()
            right_motor.hold()
            break

def rotate():

    #Turn Left
    left_motor.hold()
    right_motor.hold()
    left_motor.run(0 - turn)
    right_motor.run(turn)
    while (gyro_sensor.angle() > -90):
        continue
    if (line_sensor.color() == colour):
        gyro_sensor.reset_angle(0)
        return False

    #Turn Right
    left_motor.hold()
    right_motor.hold()
    left_motor.run(turn)
    right_motor.run(0 - turn)
    while (gyro_sensor.angle() < 90):
        continue
    print(line_sensor.color())
    if (line_sensor.color() == colour):
        gyro_sensor.reset_angle(0)
        return False

    #Turn Back
    left_motor.hold()
    right_motor.hold()
    left_motor.run(0 - turn)
    right_motor.run(turn)
    while (gyro_sensor.angle() > 0):
        continue
    run30()
    

def run30():

    # angle = 30/(math.pi * dia) * 360
    # left_motor.run_angle(speed, angle)
    # right_motor.run_angle(speed, angle)
    # while (line_sensor.color() != colour):
    #     continue

    left_motor.reset_angle(0)
    while(line_sensor.color() != colour):
        straight()
        if (left_motor.angle() > 630):
            left_motor.hold()
            right_motor.hold()
            return True

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro_sensor = GyroSensor(Port.S1)
line_sensor = ColorSensor(Port.S2)
gyro_sensor.reset_angle(0)
colour = Color.WHITE
speed = 200
turn = speed / 1.25
drift = speed / 10
dashSpeed = 20
dashDistance = 73.5
dia = 5.5

while(True):
    while (line_sensor.color() == colour):
        straight()
    if (line_sensor.color() != colour):
        dash()
        if (rotate()):
                break




