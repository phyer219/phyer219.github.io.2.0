import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,2,1000)
f = np.e**(-(1/(1-x**2)))
y = np.piecewise(x,[x<=-1,x>-1],[0,1])*np.piecewise(x,[x<=1,x>1],[1,0])*f
plt.plot(x,y)
plt.show()
