
import numpy as np
import matplotlib.pyplot as plt

def dx(x, y, r, a):
    return r*x*(1-x)-a*x*y

def dy(x, y, a, b):
    return a*y*(x-y)*(y/(b+y))

def rk4(x0, y0, r, a, b, t):
    dt = 0.001
    n = int(t/dt)
    
    x = np.zeros(n)
    y = np.zeros(n)
    time = np.linspace(0, t, n)
    
    x[0], y[0] = x0, y0
    
    for i in range(1, n):
        k1x = dt * dx(x[i-1], y[i-1], r, a)
        k1y = dt * dy(x[i-1], y[i-1], a, b)
        
        k2x = dt * dx(x[i-1] + 0.5*k1x, y[i-1] + 0.5*k1y, r, a)
        k2y = dt * dy(x[i-1] + 0.5*k1x, y[i-1] + 0.5*k1y, a, b)
        
        k3x = dt * dx(x[i-1] + 0.5*k2x, y[i-1] + 0.5*k2y, r, a)
        k3y = dt * dy(x[i-1] + 0.5*k2x, y[i-1] + 0.5*k2y, a, b)
        
        k4x = dt * dx(x[i-1] + k3x, y[i-1] + k3y, r, a)
        k4y = dt * dy(x[i-1] + k3x, y[i-1] + k3y, a, b)
        
        x[i] = x[i-1] + (k1x + 2*k2x + 2*k3x + k4x) / 6
        y[i] = y[i-1] + (k1y + 2*k2y + 2*k3y + k4y) / 6
    
    return time, x, y

# Define the figure and axes for a 2x2 grid of plots

fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # Adjust size as needed

# Parameters sets for different graphs, including different initial conditions


init = (0.05,0.1)
parameters_and_initial_conditions = [
    ((10, 5), init),
    ((5, 10), init)
]
bee=[0,0.4,1]
# Common axis range and ticks, might need adjustment based on new conditions
t=7
xlim = (0, t)
ylim = (0, 0.6)
xticks = np.arange(0, t+1, 1)
yticks = np.arange(0, 1.1, 0.1)



for i in range(2):

    axs[0,i].set_xlabel('Time', fontsize=12)
    axs[0,i].set_ylabel('Prey Density', fontsize=12)
    axs[0,i].set_xlim(xlim)
    axs[0,i].set_ylim(ylim)
    axs[0,i].set_xticks(xticks)
    axs[0,i].set_yticks(yticks)


    axs[1,i].set_xlabel('Time', fontsize=12)
    axs[1,i].set_ylabel('Predator Density', fontsize=12)
    axs[1,i].set_xlim(xlim)
    axs[1,i].set_ylim(ylim)
    axs[1,i].set_xticks(xticks)
    axs[1,i].set_yticks(yticks)





colors = ['r', 'b', 'g']
for i, ((r, a), (x0, y0)) in enumerate(parameters_and_initial_conditions, 0):
    for j , b in enumerate(bee):
        time, x, y = rk4(x0, y0, r, a, b, t)
        axs[0,i].plot(time, x, label=f'$\\beta={b}$',color=colors[j])
        axs[0,i].set_title(f'$a={a}$, $r={r}$, $x_0={x0}$, $y_0={y0}$', fontsize=12)

        axs[1,i].plot(time, y, label=f"$\\beta={b}$",color=colors[j])
        axs[1,i].set_title(f'$a={a}$, $r={r}$, $x_0={x0}$, $y_0={y0}$', fontsize=12)

        axs[0,i].legend()
        axs[1,i].legend()
    


plt.tight_layout()
plt.savefig('allee_on_predator/solver_4.pdf', dpi=300, bbox_inches='tight')


