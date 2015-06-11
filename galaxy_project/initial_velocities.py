import numpy as np

gamma = 4.4983169634398596e-06

def velocities_m(M,x,y):
    """Computes the velocities in the x and y direction of a star, m
    
    Parameters
    -------------
    M : central mass of main galaxy
    x : position of star in x-direction
    y : position of star in y-direction
    
    Returns
    ------------
    vx : velocity of star in x-direction
    vy : velocity of star in y-direction
    
    """
    rb = np.sqrt(x**2+y**2)
    v = np.sqrt((gamma*M)/rb)
    
    if x > 1e-5 or x < -1e-5:
        dx_dy = -y*((rb**2-y**2)**-0.5)
    else:
        dx_dy = 0
    
    if x < -1e-5 and y > 0 or x > 1e-5 and y < 0:
        theta = np.arctan(abs(dx_dy))
    elif x < -1e-5 and y < 0 or x > 1e-5 and y > 0:
        theta = np.arctan(abs(1/dx_dy))
    else:
        theta = 0
        
    if x < 0 and y > 0:
        vx = -v*np.sin(theta)
        vy = -v*np.cos(theta)
    elif x < 0 and y < 0:
        vx = v*np.cos(theta)
        vy = -v*np.sin(theta)
    elif x > 0 and y < 0:
        vx = v*np.sin(theta)
        vy = v*np.cos(theta)
    elif x > 0 and y > 0:
        vx = -v*np.cos(theta)
        vy = v*np.sin(theta)
    elif x == 0 and y > 0:
        vx = -v
        vy = 0
    elif x == 0 and y < 0:
        vx = v
        vy = 0
    elif x < 0 and y == 0:
        vx = 0
        vy = -v
    elif x > 0 and y == 0:
        vx = 0
        vy = v
    return vx,vy

def velocities_S(M,S,x,y):
    """Computes the velocities in the x and y direction of a disrupting galaxy, S
    Parameters
    --------------
    M : mass of main galaxy
    S : mass of disrupting galaxy
    x : position of S in x-direction
    y : position of S in y-direction
    
    Returns
    --------------
    vx : velocity of S in x-direction
    vy : velocity of S in y-direction
    """
    Rb = np.sqrt(x**2+y**2)
    v = np.sqrt((2*gamma*(M+S))/(Rb))
    dx_dy = (-y/50) 
    theta = np.arctan(abs(1/dx_dy))
    if y > 0:
        vx = v*np.cos(theta)
        vy = -v*np.sin(theta)
    elif y < 0:
        vx = v*np.cos(theta)
        vy = v*np.sin(theta)
    return vx,vy
