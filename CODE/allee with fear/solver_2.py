import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.lines as mlines

def dx(x, y, r, k, d1, a, f, e, b):
    return x*((r*x)/((a+x)*(1+f*y))-d1-k*x)-(e*x*y)/(1+b*x)

def dy(x, y, d2, c, e, b):
    return (c*e*x*y)/(1+b*x)   - d2*y


def rk4(x0, y0, t, r, k, d1, a, f, e, b, d2, c):
    dt = 0.001
    n = int(t/dt)
    
    x = np.zeros(n)
    y = np.zeros(n)
    time = np.linspace(0, t, n)
    
    x[0], y[0] = x0, y0
    
    for i in range(1, n):
        k1x = dt * dx(x[i-1], y[i-1], r, k, d1, a, f, e, b)
        k1y = dt * dy(x[i-1], y[i-1], d2, c, e, b)
        
        k2x = dt * dx(x[i-1] + 0.5*k1x, y[i-1] + 0.5*k1y, r, k, d1, a, f, e, b)
        k2y = dt * dy(x[i-1] + 0.5*k1x, y[i-1] + 0.5*k1y, d2, c, e, b)
        
        k3x = dt * dx(x[i-1] + 0.5*k2x, y[i-1] + 0.5*k2y, r, k, d1, a, f, e, b)
        k3y = dt * dy(x[i-1] + 0.5*k2x, y[i-1] + 0.5*k2y, d2, c, e, b)
        
        k4x = dt * dx(x[i-1] + k3x, y[i-1] + k3y, r, k, d1, a, f, e, b)
        k4y = dt * dy(x[i-1] + k3x, y[i-1] + k3y, d2, c, e, b)
        
        x[i] = x[i-1] + (k1x + 2*k2x + 2*k3x + k4x) / 6
        y[i] = y[i-1] + (k1y + 2*k2y + 2*k3y + k4y) / 6
    
    return time, x, y






d1 = 0.9
d2 = 0.5
k = 0.6
e = 0.7
b = 0.8
c = 0.8
r=6


a=[0.1,0.1,0.1,0.6]
f=[0.008,0.05,1,1]


x0 = 0.2
y0 = 0.4

t = 200


fig, ax = plt.subplots(1, 2, figsize=(10, 5))



for i in range(4):
    time, x, y = rk4(x0, y0, t, r, k, d1, a[i], f[i], e, b, d2, c)

    ax[0].plot(time, x, label=f'$\\alpha={a[i]}$, $f={f[i]}$', color='C'+str(i))
    ax[0].set_xlabel('Time',fontsize=12)
    ax[0].set_ylabel('Prey Density',fontsize=12)

    ax[1].plot(time, y, label=f'$\\alpha={a[i]}$, $f={f[i]}$', color='C'+str(i))
    ax[1].set_xlabel('Time',fontsize=12)
    ax[1].set_ylabel('Predator Density',fontsize=12)

    ax[0].legend()
    ax[1].legend()
fig.suptitle(f"$r={r}$, $d_1 = {d1}$, $k={k}$, $e={e}$, $b={b}$, $c={c}$, $d_2 = {d2}$, $x_0 = {x0}$, $y_0 = {y0}$", fontsize=14)

plt.savefig('solver_2.pdf',dpi=300, bbox_inches='tight')


