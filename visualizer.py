# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d


#%%
def visualizeArms(servo1Degree, servo2Degree, servo3Degree, armLength = 8, servoToCentre = 10):
    servo1 = np.deg2rad(180 - servo1Degree)
    servo2 = np.deg2rad(180 - servo2Degree)
    servo3 = np.deg2rad(180 - servo3Degree)

    l1 = 7
    l2 = 8.5
    r = 8

    x1_int = r + l1 * math.cos(servo1)
    z1_int = l1 * math.sin(servo1)

    x2_int = r + l1 * np.cos(servo2)
    z2_int = l1 * math.sin(servo2)

    x3_int = r + l1 * math.cos(servo3)
    z3_int = l1 * math.sin(servo3)

    x1 = x1_int + l2 * math.cos(math.pi - servo1)
    z1 = z1_int + l2 * math.sin(math.pi - servo1)

    x2 = x2_int + l2 * math.cos(math.pi - servo2)
    z2 = z2_int + l2 * math.sin(math.pi - servo2)

    x3 = x3_int + l2 * math.cos(math.pi - servo3)
    z3 = z3_int + l2 * math.sin(math.pi - servo3)

    def applyRotation(theta, array):
        rot_z = np.array([
            [np.cos(np.deg2rad(theta)), -np.sin(np.deg2rad(theta)), 0],
            [np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), 0],
            [0, 0, 1]
            ])

        return np.matmul(array, rot_z)

    p1data = np.array([
        [r, 0, 0],
        [x1_int, 0, z1_int],
        [x1, 0, z1]
    ])

    p2data = np.array([
        [r, 0, 0],
        [x2_int, 0, z2_int],
        [x2, 0, z2]
    ])

    p3data = np.array([
        [r, 0, 0],
        [x3_int, 0, z3_int],
        [x3, 0, z3]
    ])

    p1 = applyRotation(0, p1data)
    p2 = applyRotation(120, p2data)
    p3 = applyRotation(240, p3data)

    p1tran = np.transpose(p1)
    p2tran = np.transpose(p2)
    p3tran = np.transpose(p3)

    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

    end1 = p1tran[2]
    end2 = p2tran[2]
    end3 = p3tran[2]
    ax.plot(p1tran[0], p1tran[1], end1)
    ax.plot(p2tran[0], p2tran[1], end2)
    ax.plot(p3tran[0], p3tran[1], end3)
    

#%%
visualizeArms(50,50,40)

#%%
