import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath

x = np.linspace(0, 6, 20)
y = np.sin(x)
plt.plot(x, y, ls='none', marker='o', mfc='none')

plt.plot(x[10], y[10], marker='o', mfc='none', ms=20)
plt.plot(x[10], y[10], marker=mpath.Path.unit_regular_star(20),
         ms=25, mfc='none', mec='white')
plt.savefig('./fig1.png')
