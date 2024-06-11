import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.lines as mlines

def dx(x, y, r, a):
    return r*x*(1-x)-a*x*y

def dy(x, y, a, b):
    return a*y*(x-y)*(y/(b+y))

# Define the grid
x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x, y)

# Parameters for each plot
parameters = [
    (5, 20, 0.05),   
    (20, 5, 0.15), 
    (5, 20, 3),
    (18, 7, 2)    
]

# Create a figure and axes with a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # Adjust size as needed
axs = axs.flatten()  # Flatten the 2x2 grid to easily iterate over it

for ax, (r, a, b) in zip(axs, parameters):
    u = dx(X, Y, r, a)
    v = dy(X, Y, a, b)

    # Calculate speed
    speed = np.sqrt(u**2 + v**2)


    # Calculate speed min and max for normalization
    speed_min = np.min(speed[speed > 0])
    speed_max = np.nanmax(speed)

    norm = mcolors.LogNorm(vmin=speed_min, vmax=speed_max)

    # Create streamplot for each subplot
    strm = ax.streamplot(X, Y, u, v, color=speed, cmap='coolwarm', linewidth=0.5, arrowsize=1, density=0.5, norm=norm, broken_streamlines=False)

    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f'$r = {r}$, $a = {a}$, $\\beta = {b}$', fontsize=12)
    ax.set_xlabel('Prey Density', fontsize=12)
    ax.set_ylabel('Predator Density', fontsize=12)

    # Create a color bar for the last plot, matching the height of the plot
    # if ax == axs[-1]:  # Only for the last subplot
    #     divider = make_axes_locatable(ax)
    #     cax = divider.append_axes("right", size="5%", pad=0.05)
    #     plt.colorbar(strm.lines, cax=cax)

plt.tight_layout()  # Adjust the layout
plt.savefig('allee_on_predator/phase_space_4.pdf', dpi=300, bbox_inches='tight')
#plt.show()  # Optionally display the plot

# Note: plt.show() is commented out because execution in this environment doesn't support plot displays. 
# To view the plots, execute this script in an environment that supports matplotlib rendering, like Jupyter Notebook or a Python script run on your local machine.
