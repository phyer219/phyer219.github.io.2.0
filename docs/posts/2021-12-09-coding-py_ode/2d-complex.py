import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


domega = 1


def dC_dt(C, t, domega=domega):
    '''C = [Re c1, Im c1, Re c2, Im c2]'''
    s = np.sin(domega*t)
    c = np.cos(domega*t)
    m = [[0, 0, s, c],
         [0, 0, -c, s],
         [-s, c, 0, 0],
         [-c, -s, 0, 0]]
    return np.dot(m, C)


ts = np.linspace(0, 5, 51)
C0 = [1, 0, 0, 0]
Cs = odeint(dC_dt, C0, ts)


plt.plot(ts, Cs[:, 0]**2+Cs[:, 1]**2, 'o', label=r'numerical $|c_1(t)|^2$')
plt.plot(ts, Cs[:, 2]**2+Cs[:, 3]**2, 'o', label=r'numerical $|c_2(t)|^2$')

plt.plot(ts, np.sin(np.sqrt(domega**2/4 + 1)*ts)**2 / (1 + domega**2/4),
         label=r'analytical $|c_2(t)|^2$')
plt.ylim(0, 1.3)
plt.legend()
plt.xlabel(r'$t$')
plt.savefig('2d-complex.png')
