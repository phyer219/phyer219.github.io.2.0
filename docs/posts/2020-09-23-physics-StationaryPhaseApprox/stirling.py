import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.3, 2, 100)
y = -t + np.log(t)
plt.plot(t, y)
plt.savefig('stirling.png')
plt.show()
