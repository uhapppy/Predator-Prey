import numpy as np
import matplotlib.pyplot as plt


def logistic_growth(r, K, N0, t):
    return (K*N0*np.exp(r*t))/(K+N0*(np.exp(r*t)-1))


def exponential_growth(r, N0, t):
    return N0 * np.exp(r * t)


def derivative_logistic_growth(r, K, N):
    return r*N*(1-(N/K))


def derivative_exponential_growth(r, N):
    return r*N



N0 = 1
K = 100
r = 0.05
t = np.linspace(0, 100, 200)
N = np.linspace(0, 100, 200)

# Create a figure and a set of subplots
fig, axs = plt.subplots(1, 3, figsize=(14, 4))

# Plot for growth functions
logistic_growth_values = logistic_growth(r, K, N0, t)
exponential_growth_values = exponential_growth(r, N0, t)

axs[0].plot(t, logistic_growth_values, label="Logistic Growth",color='r')
axs[0].plot(t, exponential_growth_values, label="Exponential Growth",color='b')
axs[0].set_xlabel("$t$")
axs[0].set_ylabel("$N(t)$")
axs[0].legend()

# Plot for derivatives
# For logistic derivative, we need the population at each time t, which we already have as logistic_growth_values
# For exponential derivative, it's simply the rate times the population at each time t
logistic_derivative_values = derivative_logistic_growth(r, K, N)
exponential_derivative_values = derivative_exponential_growth(r, N)
axs[1].plot(t, logistic_derivative_values, label="Logistic Growth",color='r')
axs[1].plot(t, exponential_derivative_values, label="Exponential Growth",color='b')
axs[1].set_xlabel("$N$", fontsize=12)
axs[1].set_ylabel("$ \\frac{dN}{dt}$", fontsize=12)
axs[1].legend()

logistic_derivative_values = derivative_logistic_growth(r, K,logistic_growth_values )
exponential_derivative_values = derivative_exponential_growth(r, exponential_growth_values)
axs[2].plot(t, logistic_derivative_values, label="Logistic Growth",color='r')
axs[2].plot(t, exponential_derivative_values, label="Exponential Growth",color='b')
axs[2].set_xlabel("$t$", fontsize=12)
axs[2].set_ylabel("$ \\frac{dN}{dt}$", fontsize=12)
axs[2].legend()





# Display the plots
plt.tight_layout()
plt.savefig("images/growth.pdf", dpi=300, bbox_inches="tight")


