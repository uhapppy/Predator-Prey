import numpy as np
import matplotlib.pyplot as plt




def allee(r,N,A,K):
    return r*N*(1-(N/K))*(N-A)

def no_allee(r,N,K):
    return r*N*(1-(N/K))

def test_allee(r,b,x):
    return r*x*(1-x)*(x/(b+x))-0.1*x


r=1
K=10

A_strong=4
A_weak=0
N = np.linspace(0, 1, 200)

# Create a figure and a set of subplots

b_1=0.1
b_2=0.5


# plt.plot(N, no_allee(r*3,N,K), label="No Allee Effect (Logistic Growth)",color='r')
# plt.plot(N, allee(r,N,A_weak,K), label="Weak Allee Effect",color='b')
# plt.plot(N, allee(r,N,A_strong,K), label="Strong Allee Effect",color='g')

plt.plot(N, test_allee(r,b_1,N), label=f"{b_1}",color='r')
plt.plot(N, test_allee(r,b_2,N), label=f"{b_2}",color='b')

plt.plot([0,1],[0,0],color='black',linestyle='--')

plt.xlabel("$N$")
plt.ylabel("$\\frac{dN}{dt}$")
plt.legend()



# Display the plots
plt.tight_layout()
plt.savefig("other/allee.pdf", dpi=300, bbox_inches="tight")