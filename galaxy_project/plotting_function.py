
import matplotlib.pyplot as plt
import numpy as np

def plotter(ic,sol,n=0):
    """Plots the positions of the stars and disrupting galaxy at each t in the time array
    
    Parameters
    --------------
    ic : initial conditions
    sol : solution array
    n : integer
    
    Returns
    -------------
    """
    plt.figure(figsize=(10,10))
    
    y = np.linspace(-150,150,100)
    plt.plot(-.01*y**2+25,y,color='k',label='S path')
    
    plt.scatter(0,0,color='y',label='Galaxy M')
    plt.scatter(sol[n][0],sol[n][1],color='b',label='Galaxy S')
    for i in range(1,int(len(ic)/4)):
        a = plt.scatter(sol[n][4*i],sol[n][4*i+1],color='r')
    a.set_label('Star')
    plt.legend()
    plt.ylim(-50,50)
    plt.xlim(-50,50)
    

    
def static_plot(ic,sol,n=0):
    """Plots the positions of the stars and disrupting galaxy at a certain t in the time array
    
    Parameters
    --------------
    ic : initial conditions
    sol : solution array
    n : integer
    
    Returns
    -------------
    """
    
    plt.scatter(0,0,color='y',label='Galaxy M')
    plt.scatter(sol[n][0],sol[n][1],color='b',label='Galaxy S')
    for i in range(1,int(len(ic)/4)):
        a = plt.scatter(sol[n][4*i],sol[n][4*i+1],color='r')
    plt.ylim(-50,50)
    plt.xlim(-50,50)
    plt.tick_params(right=False,left=False,top=False,bottom=False)
    ax=plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tick_params(axis='x',labelbottom='off')
    plt.tick_params(axis='y',labelleft='off')
    
    
def com_plot(ic,sol,M,S,n=0):
    """Plots the positions of the stars, main, and disrupting galaxy relative to the center of mass at a certain t in the time
        array
        
    Parameters
    ---------------
    ic : initial condition
    sol : solution array
    M : mass of main galaxy
    S : mass of disrupting galaxy
    n : integer
    
    Returns
    --------------
    """
    plt.figure(figsize=(10,10))
    
    cm_x = (S*sol[n][0])/(M+S)
    cm_y = (S*sol[n][1])/(M+S)
    
    plt.scatter(0,0,color='g',label='Center of Mass')
    
    plt.scatter(0-cm_x,0-cm_y,color='y',label='Galaxy M')
    plt.scatter(sol[n][0]-cm_x,sol[n][1]-cm_y,color='b',label='Galaxy S')
    for i in range(1,int(len(ic)/4)):
        a = plt.scatter(sol[n][4*i]-cm_x,sol[n][4*i+1]-cm_y,color='r')
    a.set_label('Star')
    plt.legend()
    plt.ylim(-100,100)
    plt.xlim(-100,100)
    
    
def static_plot_com(ic,sol,M,S,n=0):
    """Plots the positions of the stars, main, and disrupting galaxy relative to the center of mass at a certain t in the time
        array
    Parameters
    --------------
    ic : initial conditions
    sol : solution array
    M : mass of main galaxy
    S : mass of disrupting galaxy
    n : integer
    
    Returns
    -------------
    """
    cm_x = (S*sol[n][0])/(M+S)
    cm_y = (S*sol[n][1])/(M+S)
    plt.scatter(0,0,color='g',label='Center of Mass')
    plt.scatter(0-cm_x,0-cm_y,color='y',label='Galaxy M')
    plt.scatter(sol[n][0]-cm_x,sol[n][1]-cm_y,color='b',label='Galaxy S')
    for i in range(1,int(len(ic)/4)):
        a = plt.scatter(sol[n][4*i]-cm_x,sol[n][4*i+1]-cm_y,color='r')
    plt.ylim(-100,100)
    plt.xlim(-100,100)
    plt.tick_params(right=False,left=False,top=False,bottom=False)
    ax=plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tick_params(axis='x',labelbottom='off')
    plt.tick_params(axis='y',labelleft='off')