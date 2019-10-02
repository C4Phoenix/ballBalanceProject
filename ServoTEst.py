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
ser = serial.Serial('COM4',115200)  # open serial port
vision.open(1)
#%%

#%%
center, radius, dist, speed, accel, pCenter, pRadius = vision.vision()
x_center, y_center = pCenter

max_angle = 15
edge_scaler= pRadius/max_angle
pid_x = PID(edge_scaler, 0.00, 0, output_limits=(-max_angle, max_angle))
pid_y = PID(edge_scaler, 0.00, 0, output_limits=(-max_angle, max_angle))

pid_x.setpoint = x_center
pid_y.setpoint = y_center

while True:
        while (ser.in_waiting):
                ser.read()         
        center, radius, dist, speed, accel, pop, pap = vision.vision()
        if(center == None):
                continue
        x, y = center
        # x -= x_center
        # y -= y_center

        x_angle = pid_x(x)
        y_angle = pid_y(y)

        print('Ball: ', x, y, '\tPID Output: ', x_angle, y_angle)
        # continue
        # max_angle = 30
        # x_angle = x_control / pRadius * max_angle * 1
        # y_angle = y_control / pRadius * max_angle * 1
#        # print(x_angle, y_angle)       

        time.sleep(0.01)
        xx, yy, zz = 0,0,0
        if(x_angle <= 30 and y_angle <= 30 ):
                xx,yy,zz = plateao(x_angle, y_angle, distanceFromCentre=12, HightPointY=0)
        else: print('error')
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
