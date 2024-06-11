import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.lines as mlines

def dx(x, y, g):
    return x*(1-x/g) - x*y/(1+x)

def dy(x, y, a, b):
    return b*y*(x/(1+x) - a)
# Define the grid
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(x, y)

# Parameters for each plot


a=1/2
b=2
g=5


# Create a figure and axes with a 2x2 grid
fig, ax = plt.subplots(figsize=(12, 12))  # Adjust size as needed
 # Flatten the 2x2 grid to easily iterate over it


u = dx(X, Y, g)
v = dy(X, Y, a, b)

    # Calculate speed
speed = np.sqrt(u**2 + v**2)


    # Calculate speed min and max for normalization
speed_min = np.min(speed[speed > 0])
speed_max = np.nanmax(speed)

norm = mcolors.LogNorm(vmin=speed_min, vmax=speed_max)

    # Create streamplot for each subplot
strm = ax.streamplot(X, Y, u, v, color=speed, cmap='coolwarm', linewidth=1, arrowsize=1, density=0.5, norm=norm, broken_streamlines=False)

ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('Prey Population', fontsize=12)
ax.set_ylabel('Predator Population', fontsize=12)
    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)
ax.set_title(f"$\\alpha = {a}$, $\\beta = {b}$, $\\gamma = {g}$", fontsize=14)










divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(strm.lines, cax=cax)

plt.tight_layout()  # Adjust the layout
plt.savefig('images/phase_space.pdf', dpi=300, bbox_inches='tight')
#plt.show()  # Optionally display the plot

# Note: plt.show() is commented out because execution in this environment doesn't support plot displays. 
# To view the plots, execute this script in an environment that supports matplotlib rendering, like Jupyter Notebook or a Python script run on your local machine.
