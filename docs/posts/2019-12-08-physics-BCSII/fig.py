import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

myfig = plt.figure(figsize=[8, 6])
ax = myfig.add_subplot(111)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 2)

lc = 'black'

axX = mpatches.FancyArrowPatch((-5, 0), (5, 0), mutation_scale=15,
                               arrowstyle='->', color=lc, lw=1.5)
ax.add_patch(axX)
axY = mpatches.FancyArrowPatch((0, -2), (0, 2), mutation_scale=15,
                               arrowstyle='->', color=lc, lw=1.5)
ax.add_patch(axY)

ax.annotate(r'$E$', xy=(4.5, .2), fontsize=20)
ax.annotate(r'r.h.s', xy=(.2, 1.8), fontsize=20)

x = np.linspace(-5, 0, 100)
y = np.sqrt(-x)
ax.plot(x, y)

x2 = np.linspace(-5, 5, 100)
rhsPlus = 1 + 0*x2
rhsMinus = -1 + 0*x2
ax.plot(x2, rhsPlus, '--')
ax.plot(x2, rhsMinus, '--')



myfig.savefig('fig.pdf')
myfig.savefig('fig.jpg')

