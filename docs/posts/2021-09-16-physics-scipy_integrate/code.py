import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

nodes = []


def foo(x):
    nodes.append(x)
    return np.exp(x) + np.sin(10*x)**2 + np.exp(x)**100


result = integrate.quad(foo, -1, 1, epsrel=1e-125, limit=2, full_output=1)
n = np.linspace(1, len(nodes), len(nodes))
print(len(nodes))
print(len(nodes)/21)
print(result[2]['neval'])
plt.plot(n, nodes, '*')
plt.grid()
plt.title('limit = 2')
plt.xlabel(r"$i$")
plt.ylabel("position of $i$th node")
plt.savefig('fig.png')
