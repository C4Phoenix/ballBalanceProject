#%%
'''
!pip install simple-pid
!pip install pyserial
!pip install opencv-python
!pip install imutils
'''
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
ser = serial.Serial('COM12',115200)  # open serial port
vision.open(1)
#%%
# pid_x = PID(1, 0.01, 0.15)
# pid_y = PID(1, 0.01, 0.15)

#%%
ampl = 30
while True:
        while (ser.in_waiting):
                ser.read()         
        center, radius, dist, speed, accel, pCenter, pRadius = vision.vision()
        if(center == None):
                continue
        x, y = center
        x_center, y_center = pCenter
        x -= x_center
        y -= y_center

        #x_control = pid_x(x)
        #y_control = pid_y(y)        

        max_angle = 15
        x_angle = x / pRadius * max_angle * 1
        y_angle = y / pRadius * max_angle * 1
       # print(x_angle, y_angle)       

        time.sleep(0.01)
        if(x_angle < 30 and y_angle< 30):
                xx,yy,zz = plateao(x_angle,y_angle, distanceFromCentre= 12)
        if(xx > 0 and yy > 0 and zz > 0):
                send(xx,yy,zz)

        ser.flushInput()
        ser.flushOutput()

        time.sleep(0.005)


#%%
vision.release()
ser.close()

#%%
