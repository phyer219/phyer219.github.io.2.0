import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


omega = 1


def dPsi_dt(Psi, t, omega=omega):
    re = 0
    im = omega
    m = [[re, -im], [im, re]]
    return np.dot(m, Psi)


ts = np.linspace(0, 10, 51)
phi0 = 1
Psi0 = [np.cos(phi0), np.sin(phi0)]
Psis = odeint(dPsi_dt, Psi0, ts)

plt.plot(ts, Psis[:, 0], 'o', label=r'numerical  $\mathrm{Re}\psi(t)$')
plt.plot(ts, Psis[:, 1], 'o', label=r'numerical  $\mathrm{Im}\psi(t)$')
plt.plot(ts, np.cos(omega*ts + phi0), '-',
         label=r'analytical  $\mathrm{Re}\psi(t)$')
plt.plot(ts, np.sin(omega*ts + phi0), '-',
         label=r'analytical  $\mathrm{Im}\psi(t)$')
plt.xlabel('t')
plt.legend()
plt.savefig('1d-complex.png')
