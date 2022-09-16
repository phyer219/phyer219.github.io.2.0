import numpy as np
from scipy.integrate import quad


mu = -1
E_b = 2*mu


def density(q):
    volume = q**2 / (np.pi**2)
    a = q**2/4 - 2*mu + E_b
    return volume / (np.exp(a) - 1)


n = quad(density, 0, 100, points=[0])[0]
ef_p = (3*np.pi**2 * n)**(2/3) / 2
ef_d = (6*np.pi**2 * n)**(2/3) / 2
tcef_p = 1 / ef_p
tcef_d = 1 / ef_d

print(n)
print(tcef_p, tcef_d)
