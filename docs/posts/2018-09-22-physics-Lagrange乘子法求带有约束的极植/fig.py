import numpy as np
from matplotlib import pyplot as plt

myfigure, axes = plt.subplots(1, 1, figsize=(8, 6))


r = [.5, 1, 2, 3]
c = ['b', 'g', 'y', 'pink']
theta = np.linspace(0, 2*np.pi, 100)
for i in range(4):
    x = r[i]*np.sin(theta)
    y = r[i]*np.cos(theta)
    axes.plot(x, y, c=c[i], label=r'$f(x, y)=C_%i$'%i)

x = np.linspace(-3, 3, 100)
f = np.cos(x)
axes.plot(x, f, 'r', lw=3, label=r'g(x, y)=0')
axes.legend()
axes.annotate('Maxima or Minima', xy=(0, 1), xytext=(0, 2.2),
              arrowprops=dict(arrowstyle='->', lw=3))
axes.set_xlabel(r'$x$')
axes.set_ylabel(r'$y$')
axes.set_xticklabels([])
axes.set_yticklabels([])
axes.grid()

myfigure.savefig('fig.jpg')
