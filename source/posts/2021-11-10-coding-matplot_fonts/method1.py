import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

fe = font_manager.FontEntry(fname='/usr/share/fonts/TTF/Times.TTF', name='tnr')
font_manager.fontManager.ttflist.append(fe)

plt.rcParams['font.family'] = fe.name
plt.rcParams['mathtext.fontset'] = 'cm'

x = np.linspace(0, 6, 51)
plt.plot(x, np.sin(x))
plt.title(r'Sin Function - Method 1')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\sin\theta$')
plt.savefig('method1.png')
