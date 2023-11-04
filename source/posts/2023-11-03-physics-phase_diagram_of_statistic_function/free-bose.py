import numpy as np
import matplotlib.pyplot as plt
from mpmath import polylog
from scipy.special import zeta

Ts = np.linspace(1e-12, 5, 50)
mus = np.linspace(-5, 0, 50)
n = [[Ti**(3/2)*float(polylog(s=3/2, z=np.exp(mui/Ti))) for Ti in Ts]
      for mui in mus]

levels = np.array([0.1, 1, 2, 3, 6, 10, 15])

Tc = (levels/ polylog(s=3/2, z=1))**(2/3)
CS = plt.contour(n, levels=levels, extent=[0, 5, -5, 0])
plt.plot(Tc, levels*0, 'r*', ms=10, label=r'$T_C$')
# p = CS.collections[1].get_paths()[0]
# v = p.vertices
# x = v[:,0]
# y = v[:,1]
# print(x[0], '---------------')
plt.ylim(-5, 1)
plt.plot([0, 5], [0, 0], color='black', lw=1)
plt.xlabel(r'$k_B T$')
plt.ylabel(r'$\mu$')
plt.clabel(CS)
plt.legend(loc='lower left', frameon=False)
plt.title(r'contour plot of $n(T, \mu)/\left(\frac{m}{2\pi\hbar^2}\right)^{3/2}$ for free Boson')
plt.savefig('free-bose.svg', transparent=True)