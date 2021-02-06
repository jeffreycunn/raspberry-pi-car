from flask import Flask
from flask import request
import re
import board
import time

from driver import Driver
# from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from adafruit_motorkit import MotorKit

import atexit

app = Flask(__name__)

# 'So' = Speed of outer track
# 'Si' = Speed of inner track
# 'r'  = turn radius from inner track
# 'd'  = distance between vehicle tracks.

r = 0.0762 #  (m) 3 in
d = 0.1524 # (m) 6 in

kit = MotorKit(i2c=board.I2C())

# kit.motor1.throttle = 1.0
# time.sleep(0.5)
# kit.motor1.throttle = 0
#
# mh = MotorKit(i2c=board.I2C())
# myMotor1 = mh.getMotor(1)
# myMotor2 = mh.getMotor(2)
# myMotor3 = mh.getMotor(3)
# myMotor4 = mh.getMotor(4)
#
# myMotor1.setSpeed(150)
# myMotor2.setSpeed(150)
# myMotor3.setSpeed(150)
# myMotor4.setSpeed(150)
#
# myMotor1.run(Adafruit_MotorHAT.FORWARD)
# myMotor1.run(Adafruit_MotorHAT.RELEASE)
# myMotor2.run(Adafruit_MotorHAT.FORWARD)
# myMotor2.run(Adafruit_MotorHAT.RELEASE)
# myMotor3.run(Adafruit_MotorHAT.FORWARD)
# myMotor3.run(Adafruit_MotorHAT.RELEASE)
# myMotor4.run(Adafruit_MotorHAT.FORWARD)
# myMotor4.run(Adafruit_MotorHAT.RELEASE)

# def turnOffMotors():
#     mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
#     mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
#     mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
#     mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
#
# atexit.register(turnOffMotors)

# test = Driver(0.5, -0.1, 0, r, d, myMotor1, myMotor2, myMotor3, myMotor4)
#
# print(test.i)
# print(test.j)
# print(test.k)
# print(test.r)
# print(test.d)
# print(test.direction)
# print(test.innersideFlag)
# print(test.innerSpeed)
# print(test.outerSpeed)
#
# while True:
#     test.drive()

@app.route("/")
def web_interface():
    html = open("web_interface3.html")
    response = html.read().replace('\n', '')
    html.close()
    # myMotor1.setSpeed(0)
    # myMotor2.setSpeed(0)
    # myMotor3.setSpeed(0)
    # myMotor4.setSpeed(0)
    # kit.motor1.throttle = 0
    # kit.motor2.throttle = 0
    # kit.motor3.throttle = 0
    # kit.motor3.throttle = 0
    return response

@app.route("/set_vector")
def set_vector():

    vector_str = request.args.get("vector")
    print("Received " + str(vector_str))
    # vector = [int(s) for s in vector_str.split() if s.isdigit()]
    vector = re.findall(r'\d+',vector_str)
    print(vector)
    i = float(int(vector[0]) - 125)/255
    j = float(-(int(vector[1]) - 125))/255
    #i = float(int(vector[0]) - 50)/255
    #j = float(-(int(vector[1]) - 50))/255

    print(i)
    print(j)
    test = Driver(i, j, 0, r, d, kit)
    test.drive()

    return "i = " + str(i) + ", " + str(j)

def main():
    app.run(host= '0.0.0.0')

main()
