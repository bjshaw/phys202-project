import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

gamma = 4.4983169634398596e-06

def derivs(solarray, t, M, S):
    """Computes the derivatives of the equations dictating the behavior of the stars orbiting galaxy M and the
    disrupting galaxy, S
    
    Parameters
    --------------
    solarray : solution array for the differential equations
    t : array of time values
    M : central mass of main galaxy
    S : central mass of disrupting galaxy
    
    Returns
    --------------
    derivarray : an array of the velocities and accelerations of galaxy S and stars, m
    
    """
    
    derivarray = np.zeros(len(solarray))
    
    R_x = solarray[0]
    R_y = solarray[1]
    R = np.sqrt(solarray[0]**2+solarray[1]**2)
    vR_x = solarray[2]
    vR_y = solarray[3]
    dR_x = vR_x
    dR_y = vR_y
    dvR_x = ((-gamma*(M+S)*R_x)/R**3)
    dvR_y = ((-gamma*(M+S)*R_y)/R**3)

    derivarray[0] = dR_x
    derivarray[1] = dR_y
    derivarray[2] = dvR_x
    derivarray[3] = dvR_y
    
    for n in range(1,int(len(solarray)/4)):
        r_x = solarray[4*n]
        r_y = solarray[4*n+1]
        r = np.sqrt(r_x**2+r_y**2)
        vr_x = solarray[4*n+2]
        vr_y = solarray[4*n+3]
        p_x = R_x - r_x
        p_y = R_y - r_y
        p = np.sqrt(p_x**2+p_y**2)
        dr_x = vr_x
        dr_y = vr_y
        dvr_x = -gamma*((M/r**3)*r_x-(S/p**3)*p_x+(S/R**3)*R_x)
        dvr_y = -gamma*((M/r**3)*r_y-(S/p**3)*p_y+(S/R**3)*R_y)

        derivarray[4*n] = dr_x
        derivarray[4*n+1] = dr_y
        derivarray[4*n+2] = dvr_x
        derivarray[4*n+3] = dvr_y
    
    return derivarray
    
    
    
    
def equationsolver(ic,max_time,time_step,M,S):
    """Solves the differential equations using odeint and the derivs function defined above
    
    Parameters
    -------------
    ic : initial conditions
    max_time : maximum time to be used for time array
    time_step : step size of time array
    M : central mass of main galaxy
    S : central mass of disrupting galaxy
    
    Returns
    ------------
    sol : solution array for the differential equations
    """
    t = np.linspace(0,max_time,time_step)
    sol = odeint(derivs, ic, t, args=(M,S),atol=1e-3,rtol=1e-3)
    return sol