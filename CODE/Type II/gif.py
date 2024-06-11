# Integrating troubleshooting steps into the code to ensure consistent image dimensions for GIF creation.

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable

from PIL import Image, ImageSequence

# Assume the imports are done correctly in the user's environment

# The dx and dy functions remain unchanged
def dx(x, y, g):
    return x*(1-x/g) - x*y/(1+x)

def dy(x, y, a, b):
    return b*y*(x/(1+x) - a)

# Modified function to generate a plot for a given value of a, ensuring consistent figure size and axis limits
def generate_plot(a, b, g, x, y, frame_dir, frame_index):
    X, Y = np.meshgrid(x, y)
    u = dx(X, Y, g)
    v = dy(X, Y, a, b)
    speed = np.sqrt(u**2 + v**2)
    speed_min = np.min(speed[speed > 0])
    speed_max = np.nanmax(speed)
    norm = mcolors.LogNorm(vmin=speed_min, vmax=speed_max)

    fig, ax = plt.subplots(figsize=(12, 12))
    strm = ax.streamplot(X, Y, u, v, color=speed, cmap='coolwarm', linewidth=2, arrowsize=1, density=0.7, norm=norm,broken_streamlines=False)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([0, 10])  # Explicitly setting the axis limits
    ax.set_ylim([0, 10])
    ax.set_xlabel('Prey Population', fontsize=12)
    ax.set_ylabel('Predator Population', fontsize=12)
    ax.set_title(f"$\\alpha = {a:.3g}$, $\\beta = {b}$, $\\gamma = {g}$", fontsize=14)

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(strm.lines, cax=cax)

    frame_path = os.path.join(frame_dir, f"frame_{frame_index:04d}.png")
    plt.savefig(frame_path, dpi=72, bbox_inches='tight')
    plt.close()

# Function to create the GIF from the saved frames, including a validation step for image sizes
from PIL import Image, ImageSequence

def create_gif(frame_dir, gif_path, duration=25):
    frames = []
    for file_name in sorted(os.listdir(frame_dir)):
        if file_name.endswith('.png'):
            file_path = os.path.join(frame_dir, file_name)
            with Image.open(file_path) as img:
                frames.append(img.copy())

    # Resize images if they are not the same size
    sizes = [frame.size for frame in frames]
    if len(set(sizes)) > 1:
        # Find max width and height
        max_width = max(size[0] for size in sizes)
        max_height = max(size[1] for size in sizes)
        # Resize images
        frames = [frame.resize((max_width, max_height), Image.ANTIALIAS) for frame in frames]

    # Save the frames as a GIF
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=duration, loop=0)


# A simplified version of the main function for demonstration
def main():

    x = np.linspace(0, 10, 50)
    y = np.linspace(0, 10, 50)
    
    # Parameters for each plot
    b = 2
    g = 5
    a_start = 0.0  # Starting value of a
    a_end = 1.0   # Ending value of a
    a_step = 0.001 # Increment of a
    
    frame_dir = 'frames'  # Directory to save the individual frames
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)
    
    frame_index = 0
    for a in np.arange(a_start, a_end, a_step):
        generate_plot(a, b, g, x, y, frame_dir, frame_index)
        print(f"Generated frame {frame_index}")
        frame_index += 1

    gif_path = 'predator_prey_simulation_2.gif'
    create_gif(frame_dir, gif_path, duration=25)
    
    # print(f"GIF created at {gif_path}")

# Note: The code execution for generating plots (generate_plot) and main function are commented out to prevent execution errors in this environment.
main()
