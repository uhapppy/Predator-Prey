import numpy as np
import matplotlib.pyplot as plt

def type_1(c,R):
    return c*R

def type_2(a,h,R):
    return (a*R)/(1+a*h*R)

def type_3(a,h,R,k):
    return (a*R**k)/(1+a*h*R**k)




R = np.linspace(0, 2.5, 200)

c=0.5
a=1.5
h=2
k=3



plt.plot(R, type_1(c,R), label="Type I",color='r')
plt.plot(R, type_2(a,h,R), label="Type II",color='b')
plt.plot(R, type_3(a,h,R,k), label="Type III",color='g')
plt.xlabel("Prey density")
plt.ylabel("Rate of consumption")

plt.legend()
plt.savefig("images/response.pdf", dpi=300, bbox_inches='tight')

