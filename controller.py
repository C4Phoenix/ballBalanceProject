#%%
from calculateAngle1Servo import calculateServoAngle
from visualizer import visualizeArms
import math

#%%
def plateao(X_angle, Y_angle, HightPointY=3, visualize=False, servoArmLength = 7,distanceFromCentre = 9):

    middleHightPoint = servoArmLength /2
    unresolvedServosAngle = -1
    hightAutoStepSize = 0.1

    if (HightPointY == 0):
        HightPointY = middleHightPoint

    #working with a mirror image
    X_angle /=2
    Y_angle /=2

    servo1Desired = X_angle
    servo2Desired = -X_angle/3 + 2 * -Y_angle / 3
    servo3Desired = -X_angle/3 + 2 * Y_angle / 3

    servo1, servo2, servo3 = 0,0,0

    def calculateServos():
        servo1 = calculateServoAngle(desiredAngle = servo1Desired, HightPointY = HightPointY, ServoPointX = distanceFromCentre, servoArmLength = servoArmLength)
        servo2 = calculateServoAngle(desiredAngle = servo2Desired, HightPointY = HightPointY, ServoPointX = distanceFromCentre, servoArmLength = servoArmLength)
        servo3 = calculateServoAngle(desiredAngle = servo3Desired, HightPointY = HightPointY, ServoPointX = distanceFromCentre, servoArmLength = servoArmLength)
        return servo1, servo2, servo3

    def changeMiddleHightPoint(desiredAngle,HightPointY, madeNegativeChange, madePositiveChange ):
        #bij te hoge positief moet middle punt naar beneden
        if(desiredAngle>0):
            HightPointY -= hightAutoStepSize
            madeNegativeChange = True
        else:
            HightPointY += hightAutoStepSize
            madePositiveChange = True
        return HightPointY, madePositiveChange ,madeNegativeChange

    madePositiveChange, madeNegativeChange = False, False
    prevMadePositiveChange, prevMadeNegativeChange = False, False
    prevPrevMadePositiveChange, prevPrevMadeNegativeChange = False, False
    iterations = 0
    while (servo1 <= 0 or servo2 <= 0 or servo3 <= 0):
        servo1, servo2, servo3 = calculateServos()
        iterations+=1

        prevPrevMadePositiveChange, prevPrevMadeNegativeChange = prevMadePositiveChange, prevMadeNegativeChange
        prevMadePositiveChange, prevMadeNegativeChange = madePositiveChange, madeNegativeChange
        madePositiveChange, madeNegativeChange = False, False

        if (servo1 < 0 ):
            #print('servo 1 unsolved')
            HightPointY, madePositiveChange ,madeNegativeChange = changeMiddleHightPoint(servo1Desired, HightPointY, madeNegativeChange, madePositiveChange )
        if (servo2 < 0 ):
            #print('servo 2 unsolved')
            HightPointY, madePositiveChange ,madeNegativeChange = changeMiddleHightPoint(servo2Desired, HightPointY, madeNegativeChange, madePositiveChange )
        if (servo3 < 0 ):
            #print('servo 3 unsolved')
            HightPointY, madePositiveChange ,madeNegativeChange = changeMiddleHightPoint(servo3Desired, HightPointY, madeNegativeChange, madePositiveChange )

        #print(madePositiveChange, madeNegativeChange, '-', prevMadePositiveChange, prevMadeNegativeChange, '-', prevPrevMadePositiveChange, prevPrevMadeNegativeChange, )
        if((madePositiveChange and madeNegativeChange)or (madePositiveChange and prevMadeNegativeChange and prevPrevMadePositiveChange) or (madeNegativeChange and prevMadePositiveChange and prevPrevMadeNegativeChange)): 
            print('cannot resolve angle')
            servo1, servo2, servo3 = unresolvedServosAngle, unresolvedServosAngle, unresolvedServosAngle
            break
        
    if(visualize): visualizeArms(servo1, servo2, servo3, armLength = servoArmLength, servoToCentre = distanceFromCentre)
    print('iterations: ', iterations)
    return (servo1, servo2, servo3)


# settings with distance from centre to 12
#%%
plateao(0,68 , HightPointY=0,visualize = True)

#%%
plateao(0,50 , HightPointY=0,visualize = True, distanceFromCentre= 12)

#%%
plateao(0,-50 , HightPointY=0,visualize = True)

#%%
plateao(73,0 , HightPointY=0,visualize = True)

#%%
plateao(-47,0 , HightPointY=0,visualize = True)

#%%
plateao(-33,33 , HightPointY=0,visualize = True)
#%%
plateao(33,33 , HightPointY=0,visualize = True)
#%%
plateao(-33,-33 , HightPointY=0,visualize = True)

#%%
