
#%%
import math
verbose = False
def printAngleRadians(name, angleToPrint, isRadians = True):
    toPrint = angleToPrint
    if (verbose):
        if(isRadians):
            toPrint = math.degrees(angleToPrint) 
        print(name + str( toPrint))
    return toPrint
    
#%%
# sSA & ASs
# law of sines

def calculateServoTriangle (beta, servoToMidleLength, servoArmLength, verbose = False):
    c = servoToMidleLength
    b = servoArmLength
    D = (c/b) * math.sin(beta)
    if (D > 1):
        if (verbose):
            print ('ERROR D > 1 angle not solvable')
            printAngleRadians('D: ' + str(D) + ' rad:', D)
        return -1
    gamma = math.asin(D)
    # two possibilities we need the larger angle for our model
    # moost likely gamma is always < 90
    gammaLarge = math.pi - gamma
    if(gammaLarge < gamma):
        print('didt expect gamma to be larger. reavaluate formula')
    alpha = math.pi - beta - gammaLarge

    #medeanToArmConnectionLength = b * (sin(alpha)/ sin(beta))
    return alpha

#%%
#math.degrees(calculateServoTriangle(math.radians(5),servoToMidleLength= 8, servoArmLength= 1))

#%%
def calculateServoAngle(HightPointY, ServoPointX, desiredAngle, servoArmLength):
    a = HightPointY
    b = ServoPointX
    servoToMidleLength = math.sqrt(a**2 + b**2)
    alpha2 = math.atan(a/b)
    #alpha2Deg = printAngleRadians('alpha2 ', alpha2)

    beta2 = math.atan(b/a)
    #beta2Deg = printAngleRadians('beta2 ', beta2)
    hoek2 = math.radians(90.0+ desiredAngle)
    #hoek2Deg = printAngleRadians('hoek2 ', hoek2)
    beta1 = hoek2 - beta2
    #beta1Deg = printAngleRadians('beta1 ', beta1)

    alpha1 = calculateServoTriangle(beta1, servoToMidleLength = servoToMidleLength , servoArmLength = servoArmLength)
    if (alpha1< 0): return -1
    alphaTotaal = alpha1 + alpha2

    return math.degrees(alphaTotaal)


def applyRotation(theta, array):
    rot_z = np.array([
        [np.cos(np.deg2rad(theta)), -np.sin(np.deg2rad(theta)), 0],
        [np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), 0],
        [0, 0, 1]
    ])

    return np.matmul(array, rot_z)

#def calculateServoState():
    

#%%
calculateServoAngle(HightPointY = 5, ServoPointX = 10, desiredAngle = 0, servoArmLength = 9)

