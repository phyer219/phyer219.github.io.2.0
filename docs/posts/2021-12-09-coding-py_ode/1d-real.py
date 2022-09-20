import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dy_dt(y, t):
    return 2*t*y


ts = np.linspace(0, 1, 40)
y0 = 1
ys = odeint(dy_dt, y0, ts)

plt.plot(ts, ys, 'o', label='numerical')
plt.plot(ts, np.exp(ts**2)*y0, label='analytical')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.savefig('1d-real.png')
