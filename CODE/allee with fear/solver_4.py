
import numpy as np
import matplotlib.pyplot as plt

def dx(x, y, g):
    return x*(1-x/g) - x*y/(1+x)

def dy(x, y, a, b):
    return b*y*(x/(1+x) - a)

def rk4(x0, y0, a, b, g, t):
    dt = 0.001
    n = int(t/dt)
    
    x = np.zeros(n)
    y = np.zeros(n)
    time = np.linspace(0, t, n)
    
    x[0], y[0] = x0, y0
    
    for i in range(1, n):
        k1x = dt * dx(x[i-1], y[i-1], g)
        k1y = dt * dy(x[i-1], y[i-1], a, b)
        
        k2x = dt * dx(x[i-1] + 0.5*k1x, y[i-1] + 0.5*k1y, g)
        k2y = dt * dy(x[i-1] + 0.5*k1x, y[i-1] + 0.5*k1y, a, b)
        
        k3x = dt * dx(x[i-1] + 0.5*k2x, y[i-1] + 0.5*k2y, g)
        k3y = dt * dy(x[i-1] + 0.5*k2x, y[i-1] + 0.5*k2y, a, b)
        
        k4x = dt * dx(x[i-1] + k3x, y[i-1] + k3y, g)
        k4y = dt * dy(x[i-1] + k3x, y[i-1] + k3y, a, b)
        
        x[i] = x[i-1] + (k1x + 2*k2x + 2*k3x + k4x) / 6
        y[i] = y[i-1] + (k1y + 2*k2y + 2*k3y + k4y) / 6
    
    return time, x, y

# Define the figure and axes for a 2x2 grid of plots
plt.figure(figsize=(12, 12))

# Parameters sets for different graphs, including different initial conditions
x0=0.2
y0=0.4
parameters_and_initial_conditions = [
    ((1, 2, 5), (x0, y0)),
    ((9/12, 2, 5), (x0, y0)),
    ((1/6, 2, 5), (x0, y0)),
    ((4/6, 2, 5), (x0, y0))
]

# Common axis range and ticks, might need adjustment based on new conditions
# t=50
# xlim = (0, t)
# ylim = (0, 0.6)
# xticks = np.arange(0, t+1, 1)
# yticks = np.arange(0, 1.1, 0.1)


ts = [15,70,300,500]

# Loop over each (r, a) pair with their initial conditions and plot the results
for i, ((a, b, g), (x0, y0)) in enumerate(parameters_and_initial_conditions, 1):

    t=ts[i-1]
    xlim = (0, t)
    ylim = (0, 0.6)
    xticks = np.arange(0, t+1, 1)
    yticks = np.arange(0, 1.1, 0.1)

    time, x, y = rk4(x0, y0, a, b, g, t)
    
    plt.subplot(2, 2, i)  # Update for a 2x2 grid
    plt.plot(time, x, label='Prey', color='r')
    plt.plot(time, y, label='Predator', color='b')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Population', fontsize=12)

 

    #plt.title(f'$\\alpha = {a}$, $\\beta = {b}$, $\\gamma = {g}$\n$x_0 = {x0}$, $y_0 = {y0}$', fontsize=14)  # Include initial conditions in title

    if a>g/(1+g):
        plt.title(f"$\\alpha>\\gamma/(1+\\gamma) \\rightarrow$  $\\alpha = 1$, $\\beta = {b}$, $\\gamma = {g}$", fontsize=14)
    else:
        if  (g-1)/(1+g) < a < g/(1+g):
            plt.title(f"$ (\\gamma-1)/(1+\\gamma)<\\alpha< \\gamma/(1+\\gamma) \\rightarrow$  $\\alpha = 9/12 $, $\\beta = {b}$, $\\gamma = {g}$", fontsize=14)
        elif a < (g-1)/(1+g) :
            plt.title(f"$ \\alpha<(\\gamma-1)/(1+\\gamma) \\rightarrow$  $\\alpha = 1/6$, $\\beta = {b}$, $\\gamma = {g}$", fontsize=14)
        else :
            plt.title(f"$\\alpha=(\\gamma-1)/(1+\\gamma) \\rightarrow$  $\\alpha = 4/6$, $\\beta = {b}$, $\\gamma = {g}$", fontsize=14)




    #plt.title(f'$a = {a}$, $b = {b}$\n$x_0 = {x0}$, $y_0 = {y0}$', fontsize=14)  # Include initial conditions in title
    plt.legend()
    # plt.xlim(xlim)
    # plt.ylim(ylim)
    # plt.xticks(xticks)
    # plt.yticks(yticks)

plt.tight_layout()
plt.savefig('images/solver_4.pdf', dpi=300, bbox_inches='tight')