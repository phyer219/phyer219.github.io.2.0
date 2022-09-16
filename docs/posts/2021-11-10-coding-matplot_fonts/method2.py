import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = '/usr/share/fonts/TTF/Times.TTF'  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['mathtext.fontset'] = 'cm'  # 'cm' (Computer Modern)

x = np.linspace(0, 6, 51)
plt.plot(x, np.sin(x))
plt.title(r'Sin Function - Method 2')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\sin\theta$')
plt.savefig('method2.png')
