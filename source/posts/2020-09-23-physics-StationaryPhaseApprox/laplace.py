import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 100)
y = -t**2
plt.plot(t, y, label=r'$f(x)=-x^2$')
plt.plot(t, np.exp(y), label=r'$e^{f(x)}$')
plt.plot(t, np.exp(10*y), label=r'$e^{10f(x)}$')
plt.plot(t, np.exp(100*y), label=r'$e^{100f(x)}$')
plt.legend()
plt.savefig('laplace.png')
plt.show()
