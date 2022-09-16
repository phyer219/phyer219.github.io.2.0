import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp
from scipy.integrate import quad


mp.dps = 18
print(mp)


def func(k):
    res = np.sqrt(k**4 + 1)
    res *= 4*k**2
    res += 5*k**4 + 4
    res = np.sqrt(res)
    res += -3*k**2
    return res


def mpmath_func(k_float):
    k_mpmath = mp.mpmathify(k_float)
    return func(k_mpmath)


ks = np.linspace(1000, 1001, 100)
fs = func(ks)
mp_math_fs = [mpmath_func(k) for k in ks]

plt.plot(ks, fs, '-x', label="numpy float64 type")
plt.plot(ks, mp_math_fs, label="mpmath mpf type")
plt.title('mpmath example')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend()
plt.savefig('mpmath_example.png')

print('result of numpy float64 type:', quad(mpmath_func, 0, np.inf))
print('result of mpmath mpf type:', quad(func, 0, np.inf))
