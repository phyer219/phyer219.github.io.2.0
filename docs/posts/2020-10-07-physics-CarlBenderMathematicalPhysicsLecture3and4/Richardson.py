import numpy as np
import matplotlib.pyplot as plt

n = 8
x = np.linspace(1, n, n)
y = np.zeros(n)
y[0] = 1
for i in range(n-1):
    y[i+1] = y[i] + 1/(i+2)**2


def richardson2(y):
    """2nd order Richardson extrapolation"""
    n = y.shape[0]
    r2 = np.full(n, np.NaN)
    for i in range(n-2):
        r2[i] = (i+1)**2 * y[i] - 2*(i+2)**2 * y[i+1] + (i+3)**2 * y[i+2]
        r2[i] *= .5
    return r2
r2 = richardson2(y)

plt.plot(x, np.full(n, np.pi**2/6), label=r'$\pi^2/6$')
plt.plot(x, y, 'o', label=r'$S_N$')
plt.plot(x, r2, 'o', label=r'$R_2$')
plt.title(r'Richardson extrapolation of $\sum \frac{1}{n^2}$')
plt.legend()
plt.savefig('Richardson.jpg')
plt.show()
