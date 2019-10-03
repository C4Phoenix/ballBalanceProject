#%%
# Imports
import cv2
import imutils
import time as Time
import math
import numpy as np
from collections import deque

#%%
# Variables
ballDiameter = 40  # mm
capSrc = 0
colorLower = (4, 165, 190)
colorUpper = (30, 255, 255)
minRadius = 10
trailLength = 64
trail = deque(maxlen=trailLength)
prevTrack = (0, (0, 0), 0, 0)  # timestamp, center, radius, speed
color = (0, 0, 0)

#%%
# Functions
def handleKeyboard(key):
    if key == 27:  # Esc
        global done
        done = True

def track(frame):
    global minRadius

    mask = cv2.inRange(frame, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))

        if radius > minRadius:
            return center, radius

    return None, None

def trackMotion(time, center, radius):
    global prevTrack
    prevTime, prevCenter, prevRadius, prevSpeed = prevTrack

    dist = speed = accel = 0

    if prevTime > 0 and center is not None and prevCenter is not None:
        dTime = time - prevTime
        dist = calcDist(center, prevCenter) * calcRatio((radius + prevRadius) / 2)
        speed = calcSpeed(dist, dTime)
        accel = calcAccel(speed - prevSpeed, dTime)

    prevTrack = time, center, radius, speed

    return dist, speed, accel

def trackPlatform(frame):
    mask = cv2.inRange(frame, (0, 0, 125), (100, 75, 255))
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))

        if radius > 100:
            return center, radius

    return None, None

def drawTracking(center, radius, frame):
    global trail, trailLength, color

    if center is not None and radius is not None:
        cv2.circle(frame, center, int(radius),
            (0, 255, 255), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

    trail.appendleft(center)

    for i in range(1, len(trail)):
        if trail[i - 1] is None or trail[i] is None:
            continue
 
        thickness = int(np.sqrt(trailLength / float(i + 1)) * 2.5)
        cv2.line(frame, trail[i - 1], trail[i], color, thickness)

def calcRatio(radius):
    global ballDiameter
    return ballDiameter / (radius * 2)

def calcDist(center, prevCenter):
    x, y = center
    prevX, prevY = prevCenter
    dX = x - prevX
    dY = y - prevY
    return math.sqrt(dX**2 + dY**2)

def calcSpeed(dist, dTime):
    return dist / dTime

def calcAccel(dSpeed, dTime):
    return dSpeed / dTime

#%%
# Set capture source
def open(cam):
    global cap
    capSrc = cam
    cap = cv2.VideoCapture(capSrc)

#%%
def vision():
    global ballDiameter, capSrc, colorLower, colorUpper, minRadius, trailLength, trail, prevTrack, color
    dist = speed = accel = 0
    if not cap.isOpened():
        cap.open(capSrc)

    retval, raw = cap.read()

    if retval == 0:
        return (0, 0), 0, 0, 0, 0

    time = int(round(Time.time() * 1000))

    blurred = cv2.GaussianBlur(raw, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    tracked = raw.copy()
    center, radius = track(hsv)
    pCenter, pRadius = trackPlatform(hsv)
    drawTracking(center, radius, tracked)
    drawTracking(pCenter, pRadius, tracked)

    prevTime, prevCenter, prevRadius, prevSpeed = prevTrack

    if time - prevTime >= 100:
        dist, speed, accel = trackMotion(time, center, radius)
        # print('Dist: %.2fmm\tSpeed: %.2fmm/ms\tAccel: %.2fmm/ms^2' % (dist, speed, accel))
        color = (0, 0, speed * 255)

    cv2.putText(tracked,'Dist: %.2fmm\tSpeed: %.2fmm/s\tAccel: %.2fmm/ms^2' % (dist, speed * 1000, accel), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0))
    cv2.imshow("Tracked", tracked)

    handleKeyboard(cv2.waitKey(1))
    
    return center, radius, dist, speed, accel, pCenter, pRadius


#%%
# Release capture source
def release():
    global cap
    cv2.destroyAllWindows()
    cap.release()

#%%
