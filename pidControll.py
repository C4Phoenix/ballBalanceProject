# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # Moving Ball (2D)
# 
# ![alt-text](data:image/png;base64,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)
# 
# # Rotational and translational kinetic energy
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=F_{rx}%2bF_{tx}%2bF_{r}=mgSin%28\alpha%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=\frac{I}{r^2}\ddot{x}%2bm\ddot{x}%2bf_{r}mgCos%28\alpha%29=mgSin%28\alpha%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=I=\frac{2}{3}mr^2&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# # Final equation of motion
# 
# This equation of motion only holds when there is no slip AND when the ball does not have any influence on the angle of the surface. Also the air resistence is neglected. If you would, you could add this to the equation. But ... you need to derive it first!
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=\ddot{x}=\frac{3}{5}gSin%28\alpha%29-\frac{3}{5}f_{r}gCos%28\alpha%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# # State space
# 
# We need to write this equations into a set of independent differential equations.
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=\dot{x_{1}}[i]=x_{2}[i]&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=\dot{x_{2}}[i]=\frac{3}{5}gSin%28\alpha%29-\frac{3}{5}f_{r}gCos%28\alpha%29%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=x_{1}[i]=x_{1}[i-1]%20%2b%20\dot{x}_{1}[i]\triangle{T}&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
# 
# ![equation](http://www.sciweavers.org/tex2img.php?eq=x_{2}[i]=x_{2}[i-1]%20%2b%20\dot{x}_{2}[i]\triangle{T}%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev)

#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

# System paramters
m = 0.0027 # 2.7 gr
g = 9.8 # gravity acceleration
fr = 0.01 # friction
ts = 0.001 #time step we would like to perform the calculation

# Initial condition of the system, the surface start at an angle
# The acceleration and velocity is zero at this moment.
x0 = [0, 0]
x0dot = [0, 0]
u = -1*math.pi/180 # u = alpha

# The model that delivers the dx/dt matrix as defined above
# This model is used by odeint
def model(x, t, u):
    xdot = np.zeros(2)   
    
    xdot[0] = x[1]
    xdot[1] = (3/5)*g*np.sin(u)-(3/5)*fr*g*np.cos(u)
        
    return xdot

# Some results for plotting
position = []
velocity = []
time     = []

x = x0
for i in range (0, int(10/ts)):
    y = odeint(model, x, [0, ts], args=(u,))
    x = y[1]
    
    if ( i % (0.1/ts) == 0 ):
        position.append(y[1][0])
        velocity.append(y[1][1])
        time.append(i * ts)
        
        if ( i*ts > 5 ):
            u = 12 * math.pi/180

fig, ax = plt.subplots()
line, = plt.plot(time, position, label='Slinger') # blue
line, = plt.plot(time, velocity, label='Slinger') # blue

#%% [markdown]
# # Controlling the ball

#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

# System paramters
m = 0.0027 # 2.7 gr
g = 9.8 # gravity acceleration
fr = 0.01 # friction
ts = 0.001 #time step we would like to perform the calculation

# Initial condition of the system, the surface start at an angle
# The acceleration and velocity is zero at this moment.
x0 = [0, 0]
x0dot = [0, 0]
u = -1*math.pi/180 # u = alpha

# The model that delivers the dx/dt matrix as defined above
# This model is used by odeint
def model(x, t, u):
    xdot = np.zeros(2)   
    
    xdot[0] = x[1]
    xdot[1] = (3/5)*g*np.sin(u)
    
    if ( x[1] > 0 ):
        xdot[1] += -(3/5)*fr*g*np.cos(u)
        
    return xdot

# Some results for plotting
position = []
velocity = []
errors   = []
angles   = []
time     = []

# Controller
ref = 2
Kp = 0.01 #0.1
Ki = 0.000001#0.0000000001
Kd = 10 # 10
esum = 0
perr = 0
maxsum = 100000

x = x0
for i in range (0, int(25/ts)):
    # Controller
    error = ref - x[0]
    esum = esum + error
    derror = error - perr
    
    if ( i == 0 ):
        derror = 0
    
    u      = Kp * error + Ki * esum + Kd * derror
    perr   = error
    
    #if ( esum > maxsum ):
    #    esum = maxsum
    
    y = odeint(model, x, [0, ts], args=(u,))
    x = y[1]
    
    if ( i % (0.1/ts) == 0 ):
        position.append(y[1][0])
        velocity.append(y[1][1])
        errors.append(error)
        angles.append(u*200)
        time.append(i * ts)
        
        if ( i*ts > 13 ):
            ref = 5.6

fig, ax = plt.subplots()
line, = plt.plot(time, position, label='Slinger') # blue
line, = plt.plot(time, velocity, label='Slinger') # orange
line, = plt.plot(time, errors, label='Slinger') # green
line, = plt.plot(time, angles, label='Slinger') # red
