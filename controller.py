#%%
from calculateAngle1Servo import calculateServoAngle
from visualizer import visualizeArms
import math

#%%
def plateao(X_angle, Y_angle, HightPointY=3, visualize=False):
    servoArmLength = 7
    distanceFromCentre = 12

    #working with a mirror image
    X_angle /=2
    Y_angle /=2

    servo1Desired = X_angle
    servo2Desired = -X_angle/3 + 2 * -Y_angle / 3
    servo3Desired = -X_angle/3 + 2 * Y_angle / 3

    servo1 = calculateServoAngle(desiredAngle = servo1Desired, HightPointY = HightPointY, ServoPointX = distanceFromCentre, servoArmLength = servoArmLength)
    servo2 = calculateServoAngle(desiredAngle = servo2Desired, HightPointY = HightPointY, ServoPointX = distanceFromCentre, servoArmLength = servoArmLength)
    servo3 = calculateServoAngle(desiredAngle = servo3Desired, HightPointY = HightPointY, ServoPointX = distanceFromCentre, servoArmLength = servoArmLength)

    if (servo1 < 0 ): print('servo 1 unsolved')
    if (servo2 < 0 ): print('servo 2 unsolved')
    if (servo3 < 0 ): print('servo 3 unsolved')

    if(visualize): visualizeArms(servo1, servo2, servo3, armLength = servoArmLength, servoToCentre = distanceFromCentre)

    return (servo1, servo2, servo3)
#%%
plateao(0, -30, HightPointY= 3.5,visualize = True)

#%%
