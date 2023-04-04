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


res, nc, vc = quad_recorded(np.sin, 0, np.pi, points=[.5])
plt.plot(nc, vc, '*')
print(res)
plt.savefig('quad_recorded.png', transparent=True)
