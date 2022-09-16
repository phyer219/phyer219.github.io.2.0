import numpy as np
import matplotlib.pyplot as plt

n=50
x = np.linspace(1, n, n)
y = np.zeros(n)
y[0] = 1
for i in range(n-1):
    y[i+1] = y[i] + (-1)**(i+1) * 1/(i+2) 
plt.plot(x, y, 'r')
plt.plot(x, 0*x+np.log(2), 'g')
print(y[-1])
plt.savefig('log2.jpg')
plt.show()
