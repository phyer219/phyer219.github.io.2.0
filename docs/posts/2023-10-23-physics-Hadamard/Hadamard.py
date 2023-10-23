import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def quad_recorded(func, *args, **kwargs):
    """
    use scipy.integrate.quad, but return the results with additional
    information "nc" and "vc".

    Returns:
        inte_res: the return of scipy.integrate.quad
              nc: the points calculated
              vc: the calculated functiona values
    """
    def func_recorded(x, node_container, value_container):
        res = func(x)
        node_container.append(x)
        value_container.append(res)
        return res
    nc = []
    vc = []
    inte_res = quad(lambda x: func_recorded(x, node_container=nc,
                                            value_container=vc),
                    *args, **kwargs)
    idx = np.argsort(np.array(nc))
    nc = np.array(nc)[idx].tolist()
    vc = np.array(vc)[idx].tolist()
    return inte_res, nc, vc


def f(r, z):
    return 1/(1 + z**2)

def foo(r, z):
    return f(r, z)/(r**2 + z**2)


# check the first term in expansion
r = 0.01
res, nc, vc = quad_recorded(lambda z: foo(r, z), -2, 2, points=[0])
plt.plot(nc, vc, '*')
print('numeric:', res)
print('analytic:', np.pi/r*f(0, 0))
plt.savefig('first-term.png', transparent=True)
plt.clf()


# calculate the Hadamard finite part
def fini(z):
    return f(0, z)/z**2 - f(0, 0)/z**2

res, nc, vc = quad_recorded(fini, -2000, 2000, points=[0])
plt.plot(nc, vc, '*')
# print('numeric:', res)
# print('analytic:', np.pi/r*f(0, 0))
print(res)
plt.savefig('finite-part.png', transparent=True)
