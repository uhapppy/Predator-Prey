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
a=0.1
f=1

x0 = 0.2
y0 = 0.4

t = 200


fig, ax = plt.subplots(1, 2, figsize=(10, 5))



x = np.linspace(0, 20, 50)
y = np.linspace(0, 20, 50)
X, Y = np.meshgrid(x, y)


u = dx(X, Y, r, k, d1, a, f, e, b)
v = dy(X, Y, d2, c, e, b)

# Calculate speed
speed = np.sqrt(u**2 + v**2)


# Calculate speed min and max for normalization
speed_min = np.min(speed[speed > 0])
speed_max = np.nanmax(speed)

norm = mcolors.LogNorm(vmin=speed_min, vmax=speed_max)

    # Create streamplot for each subplot
strm = ax[0].streamplot(X, Y, u, v, color=speed, cmap='coolwarm', linewidth=1, arrowsize=1, density=0.7, norm=norm, broken_streamlines=False)

#ax[0].set_aspect('equal', adjustable='box')
ax[0].set_xlabel('Prey Density', fontsize=12)
ax[0].set_ylabel('Predator Density', fontsize=12)



time, x, y = rk4(x0, y0, t, r, k, d1, a, f, e, b, d2, c)

ax[1].plot(time, x, label='Prey', color='red')
ax[1].plot(time, y, label='Predator', color='blue')
ax[1].set_xlabel('Time',fontsize=12)
ax[1].set_ylabel('Population Density',fontsize=12)

ax[1].legend()
fig.suptitle(f"$r={r}$, $a={a}$, $f={f}$ \n $d_1 = {d1}$, $k={k}$, $e={e}$, $b={b}$, $c={c}$, $d_2 = {d2}$", fontsize=14)

plt.savefig('Phase_and_solution_case_7.pdf',dpi=300, bbox_inches='tight')


