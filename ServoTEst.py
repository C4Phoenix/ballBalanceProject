#%%
# !pip install simple-pid
# !pip install pyserial
# !pip install opencv-python
# !pip install imutils
#%%
import serial
import time
import random
import math
import vision
from controller import plateao
from simple_pid import PID

#%%
def send(angle1,angle2,angle3):
    print('x:',angle1,'y:',angle2, 'z:', angle3)
    sendOne(angle1,0)
    sendOne(angle2,120)
    sendOne(angle3,240)

def sendOne(angle,id):
    s = 's:' + str(id) + ':' + str(angle) + '\n'
    ser.write(s.encode())

def calcAndSend(x,y):
    x,y,z = plateao(x,y,visualize=True)
    print(x,y,z)
    send(int(x),int(y),int(z))

def rotatoes():
    i=0
    numbers = range(10,30)
    while True:

        send(numbers[i%20],numbers[(i+1)%20],numbers[(i+2)%20])
        
        i += 1

        time.sleep(0.5)
        
#%%
ser = serial.Serial('COM5',115200)  # open serial port
vision.open(0)
max_angle = 30
#%%

#%%
send(0, 0, 0)
time.sleep(0.1)
center, radius, dist, speed, accel, pCenter, pRadius = vision.vision()
x_center, y_center = pCenter

pid_x = PID(1, 0, .25)
pid_y = PID(1, 0, .25)

while True:
        while (ser.in_waiting):
                ser.read()
        center, radius, dist, speed, accel, pop, pap = vision.vision()
        if(center == None):                
                send(0, 0, 0)
                continue
        x, y = center
        x -= x_center
        y -= y_center

        x_angle = pid_x(x) / pRadius * -max_angle
        y_angle = pid_y(y) / pRadius * -max_angle

        print('Ball: ', x, y, '\tPID Output: ', x_angle, y_angle)

        # # x_angle = x_control / pRadius * max_angle * 1
        # # y_angle = y_control / pRadius * max_angle * 1
        # # print(x_angle, y_angle)       

        time.sleep(0.01)
        xx, yy, zz = 0,0,0
        if(x_angle <= max_angle and x_angle >= -max_angle and y_angle <= max_angle and y_angle >= -max_angle):
                xx,yy,zz = plateao(x_angle, y_angle, distanceFromCentre=12, HightPointY=0)
        if(xx < 0): xx = 0
        if(xx > 70): xx = 70
        
        if(yy < 0): yy = 0
        if(yy > 70): yy = 70
        
        if(zz < 0): zz = 0
        if(zz > 70): zz = 70
        
        send(70-xx,70-zz,70-yy)

        ser.flushInput()
        ser.flushOutput()

        time.sleep(0.005)


#%%
vision.release()
ser.close()

#%%
while True:
        for i in range (0, 70):
                send(i, i, i)
                
                while (ser.in_waiting):
                        ser.read()   
                time.sleep(0.1)

#%%
