import numpy as np
import matplotlib.pyplot as plt

#import data 

data = np.loadtxt('data.txt')
time = data[:,0]
x = data[:,1]
y = data[:,2]

plt.plot(time, x, label='Snowshoe hare (Prey)', color='red')
plt.plot(time, y, label='Lynx (Predator)', color='blue')
plt.xlabel('Years')
plt.ylabel('Thousands furs')
plt.legend()

plt.savefig('images/real_data.pdf', dpi=300, bbox_inches='tight')

