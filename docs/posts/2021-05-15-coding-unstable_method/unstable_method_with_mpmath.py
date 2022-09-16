import numpy as np
from mpmath import mp
import matplotlib.pyplot as plt


mp.dps = 20
print(mp)


def unstable(n: int) -> float:
    p = []
    p.append(1)
    p.append((mp.sqrt(5) - 1) / 2)
    for i in range(n-1):
        i += 1
        p.append(p[i-1] - p[i])
    return p[-1]


def stable(n: int) -> float:
    return ((np.sqrt(5) - 1) / 2)**n


n = 80
x = []
y_unstable = []
y_stable = []
for i in range(n):
    i += 1
    x.append(i)
    y_unstable.append(unstable(i))
    y_stable.append(stable(i))

plt.plot(x, y_unstable, '-x', label="unstable method with mpmath")
plt.plot(x, y_stable, label="stable")
plt.xlabel(r'$n$')
plt.ylabel(r'$\left(\frac{\sqrt{5} - 1}{2}\right)^n$')
plt.legend()
plt.savefig('unstable_method_with_mpmath.png')
