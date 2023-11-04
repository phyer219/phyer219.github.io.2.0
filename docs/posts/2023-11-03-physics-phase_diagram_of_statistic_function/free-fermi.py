import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from mpmath import polylog
from scipy.special import zeta

Ts = np.linspace(1e-2, 5, 50)
mus = np.linspace(-5, 5, 50) # mu=0 is a pole
n = [[Ti**(3/2)*float(-polylog(s=3/2, z=-np.exp(mui/Ti)).real) for Ti in Ts]
      for mui in mus]

levels = np.array([0.1, 0.5, 1, 2, 5, 7])
Ef = (levels*6*np.pi**2)**(2/3) / (4*np.pi)
Tc = (levels/ polylog(s=3/2, z=1))**(2/3)
CS = plt.contour(n, levels=levels, extent=[Ts[0], Ts[-1], mus[0], mus[-1]])
plt.plot(levels*0, Ef, 'r*', ms=10, label=r'$E_F$')

plt.xlabel(r'$k_B T$')
plt.ylabel(r'$\mu$')
plt.legend(frameon=False)

plt.plot([-1, 5], [0, 0], lw=1, color='black')
plt.plot([0, 0], [-5, 5], lw=1, color='black')
plt.xlim(-1, 5)
plt.clabel(CS)
plt.title(r'contour plot of $n(T, \mu)/\left(\frac{m}{2\pi\hbar^2}\right)^{3/2}$ for free Fermion')

plt.savefig('free-fermi.svg', transparent=True)