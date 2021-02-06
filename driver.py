import math

class Driver(object):

    def __init__(self, i, j, k, r, d, kit):  # i, j, k is a unit vector of values 0 to 1
        self.i = i
        self.j = j
        self.k = k
        self.r = r
        self.d = d
        self.myMotor1 = kit.motor1
        self.myMotor2 = kit.motor2
        self.myMotor3 = kit.motor3
        self.myMotor4 = kit.motor4

        if i < -0.1:
            self.innersideFlag = 'L'
        elif i > 0.1:
            self.innersideFlag = 'R'
        else:
            self.innersideFlag = 'LR'

        self.direction = 1
        if j < 0:
            self.direction = -1

        if abs(j) < 0.1:
            self.innerSpeed = 0
            self.outerSpeed = 0
        else:
            self.innerSpeed = abs(j*255)/255

            self.outerSpeed = (self.innerSpeed * ((r + d) / r))

        print("A J2G2 driver object is created")


    def drive(self):

        if self.innersideFlag == 'L':
            print('Left Activated')
            print(self.direction)
            print(self.outerSpeed)
            print(self.innerSpeed)
            print(self.direction*abs(self.outerSpeed))
            print(self.direction*abs(self.innerSpeed))
            self.myMotor1.throttle = self.direction*abs(self.outerSpeed)

            self.myMotor2.throttle = self.direction*abs(self.outerSpeed)

            self.myMotor3.throttle = self.direction*abs(self.innerSpeed)

            self.myMotor4.throttle = -self.direction*abs(self.innerSpeed)

        elif self.innersideFlag == 'R':
            print('Right Activated')
            self.myMotor1.throttle = self.direction*abs(self.innerSpeed)

            self.myMotor2.throttle = self.direction*abs(self.innerSpeed)

            self.myMotor3.throttle = self.direction*abs(self.outerSpeed)

            self.myMotor4.throttle = -self.direction*abs(self.outerSpeed)

        elif self.innersideFlag == 'LR':
            print('Center Activated')

            self.myMotor1.throttle= self.direction*abs(self.innerSpeed)

            self.myMotor2.throttle = self.direction*abs(self.innerSpeed)

            self.myMotor3.throttle = self.direction*abs(self.innerSpeed)

            self.myMotor4.throttle = -self.direction*abs(self.innerSpeed)



