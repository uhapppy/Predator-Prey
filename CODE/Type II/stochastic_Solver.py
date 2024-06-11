import numpy as np
import matplotlib.pyplot as plt

def dx(x, y, g):
    return x * (1 - x / g) - x * y / (1 + x)

def dy(x, y, a, b):
    return b * y * (x / (1 + x) - a)

def sigma_x(x, y, sigma_x0):
    return sigma_x0 * x  # Noise proportional to the current state of x

def sigma_y(x, y, sigma_y0):
    return sigma_y0 * y  # Noise proportional to the current state of y

def stochastic_runge_kutta(x0, y0, g, a, b, sigma_x0, sigma_y0, T, dt):
    N = int(T / dt)
    t = np.linspace(0, T, N)
    x = np.zeros(N)
    y = np.zeros(N)
    x[0] = x0
    y[0] = y0
    prey_negative = False
    predator_negative = False
    
    for i in range(1, N):


        if x[i-1] < 0:
            print("x is negative at time", t[i-1])
            x[i-1] = 0
            prey_negative = True


        if y[i-1] < 0:
            print("y is negative at time", t[i-1])
            y[i-1] = 0
            predator_negative = True


        xi = x[i-1]
        yi = y[i-1]

        dx1 = dx(xi, yi, g)
        dy1 = dy(xi, yi, a, b)

        # sx1 = sigma_x(xi, yi, sigma_x0)
        # sy1 = sigma_y(xi, yi, sigma_y0)

        # dWx = np.random.normal(0, np.sqrt(dt))
        # dWy = np.random.normal(0, np.sqrt(dt))

        sx1 = 1
        sy1 = 1

        dWx = np.random.normal(0, sigma_x0)
        dWy = np.random.normal(0, sigma_y0)

        x_tilde = xi + dx1 * dt + sx1 * dWx
        y_tilde = yi + dy1 * dt + sy1 * dWy

        dx2 = dx(x_tilde, y_tilde, g)
        dy2 = dy(x_tilde, y_tilde, a, b)
        
        sx2 = sigma_x(x_tilde, y_tilde, sigma_x0)
        sy2 = sigma_y(x_tilde, y_tilde, sigma_y0)

        

        x[i] = xi + 0.5 * (dx1 + dx2) * dt + 0.5 * (sx1 + sx2) * dWx
        y[i] = yi + 0.5 * (dy1 + dy2) * dt + 0.5 * (sy1 + sy2) * dWy

        if prey_negative:
            x[i] = 0
        if predator_negative:
            y[i] = 0



    return t, x, y

# Parameters
x0 = 10    # initial x value
y0 = 5    # initial y value
g = 5     # parameter in dx
a = 1/6   # parameter in dy
b = 2   # parameter in dy
sigma_x0 = 0.01  # noise strength for x
sigma_y0 = 0.01 # noise strength for y
T = 300    # total time
dt = 0.01  # time step

t_values, x_values, y_values = stochastic_runge_kutta(x0, y0, g, a, b, sigma_x0, sigma_y0, T, dt)

# Plotting
plt.plot(t_values, x_values, label='Prey' ,color="red")
plt.plot(t_values, y_values, label='Predator', color="blue")
plt.xlabel('Time')
plt.ylabel('Population density')
plt.title(f"$\\sigma_x = {sigma_x0}$, $\\sigma_y = {sigma_y0}$")
plt.legend()
plt.savefig('stochastic_simulation_4.pdf', dpi=300, bbox_inches='tight')
