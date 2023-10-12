import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax00 = fig.add_subplot(1, 2, 1)
ax00twin = ax00.twiny()
ax01 = fig.add_subplot(1, 2, 2)

x = np.linspace(0, 6, 100)
xtwin = np.linspace(0, 60, 100)
ax00.plot(x, np.sin(x), 'b-')
# ax00twin.plot(xtwin, np.cos(0.1*xtwin), 'r--')
ax00twin.set_xticks([0, 100, 200])
ax00.set_xlim(0, 6)
ax00twin.set_xlim(0, 200)

ax01.plot(x, np.cos(x))
ax01.secondary_xaxis(location='top', functions=(lambda x: 2*x, lambda x: 2*x))
fig.savefig('double_ax.png', transparent=True)