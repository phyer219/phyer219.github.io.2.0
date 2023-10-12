import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import matplotlib as mpl


def newcmap(old):
    old_map = mpl.colormaps[old]
    cut1 = old_map(np.linspace(0, 0.5, 50))
    cut2 = old_map(np.linspace(0.5, 1, 500))
#     cut3 = old_map(np.linspace(0.6, 1, 10))
    cutall = np.concatenate([cut1, cut2])
    return ListedColormap(cutall)


print(newcmap('jet'))
plt.imshow(np.random.randn(100, 100), cmap=newcmap('jet'))
plt.colorbar()
plt.savefig('newcmap.png', transparent=True)