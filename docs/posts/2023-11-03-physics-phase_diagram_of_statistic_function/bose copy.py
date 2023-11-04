import numpy as np
import matplotlib.pyplot as plt
from mpmath import polylog
from scipy.special import zeta

Ts = np.linspace(1e-12, 5, 50)
mus = np.linspace(-5, 0, 50) # mu=0 is a pole
n = [[Ti**(3/2)*float(polylog(s=3/2, z=np.exp(mui/Ti))) for Ti in Ts]
      for mui in mus]
X, Y = np.meshgrid(Ts, mus)
print(n)
# plt.imshow(n, origin='lower', extent=[-1, 0, 0, 1])
# plt.colorbar()
# plt.show()
levels = np.array([0.1, (4*np.pi)**(3/2)/(6*np.pi**2), 2, 3, 6, 10, 15])
Tc = (levels/ polylog(s=3/2, z=1))**(2/3)
CS = plt.contour(X, Y, n, levels=levels)

p = CS.collections[1].get_paths()[0]
v = p.vertices
x = v[:,0]
y = v[:,1]
print(x[0], '---------------')

plt.plot(x, y, 'x')
plt.xlabel(r'$k_B T$')
plt.ylabel(r'$\mu$')
#plt.ylim(-5, 0)
plt.plot(Tc, levels*0, 'r.', ms=15)
plt.clabel(CS)
plt.title(r'contour plot of $n(T, \mu)/\left(\frac{m}{2\pi\hbar^2}\right)^{3/2}$ for Boson')
#plt.show()




# Ts = np.linspace(1e-2, 1, 5)
# mus = np.linspace(-1, 1, 5)
# n = [[-Ti**(3/2)*float(polylog(s=3/2, z=-np.exp(mui/Ti)).real) for mui in mus]
#       for Ti in Ts]
# X, Y = np.meshgrid(mus, Ts)
# print(n)
# # plt.imshow(n, origin='lower', extent=[-1, 0, 0, 1])
# # plt.colorbar()
# # plt.show()
# CS = plt.contour(X, Y, n)
# plt.clabel(CS)
plt.savefig('bose.svg', transparent=False)