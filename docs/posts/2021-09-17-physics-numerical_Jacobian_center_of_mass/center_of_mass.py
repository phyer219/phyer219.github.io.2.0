import numpy as np
from scipy.integrate import quad
from scipy.integrate import nquad


def l_bound(phi_minus):
    if phi_minus > 0:
        l_bound = 4*np.pi - 2*phi_minus
    else:
        l_bound = 4*np.pi + 2*phi_minus
    return l_bound


def f(phi_minus):
    res = phi_minus + 2*phi_minus**2 + 3*phi_minus**3 - 3**phi_minus
    return res


center = quad(lambda phi_minus: l_bound(phi_minus)*f(phi_minus)/2, -2*np.pi,
              2*np.pi)


normal = nquad(lambda phi_k, phi_q: f(phi_k-phi_q), [[0, 2*np.pi],
                                                     [0, 2*np.pi]])
print(center)
print(normal)
