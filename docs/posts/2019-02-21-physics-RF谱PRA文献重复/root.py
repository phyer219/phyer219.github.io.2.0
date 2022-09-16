import numpy as np
from matplotlib import pyplot as plt

delta = .5
N = 100
o = np.linspace(-2, 2, N)
q = np.linspace(-2, 2, N)
fig, ax = plt.subplots()
#line = ax.plot(o,q)
#ax3 = fig.add_axes([0.1, 0.1, 0.2, 0.2])

#ax.plot(o,o*0+1)
#ax.plot(o,o*0)
ax.plot(o*0+delta,o, color = 'green')
ax.plot(o*0+delta-.5,o, color = 'gray', linestyle = '--')
ax.plot(delta - q**2/2, q, 'r', label = r'$\~\omega = \~\delta - \frac{\~q^2}{2}$')
ax.plot(delta - (q-1)**2/2, q, color = 'blue', label = r'$\~\omega = \~\delta - \frac{(\~q-1)^2}{2}$')

ax.text(-1.2, .5, r'$r_1,r_2\notin [0,1]$', {'fontsize':20})
ax.text(.05, .95, r'$r_2\in [0,1]$', {'fontsize':20})
ax.text(.07, .05, r'$r_1\in [0,1]$', {'fontsize':20})
ax.text(1, .5, r'no root', {'fontsize':20})

ax.arrow(1, .25, -.55, .25, width = .01)
ax.text(1, .25, r'$r_1,r_2\in [0,1]$', {'fontsize':20})

#ax.set_xlim(0,4*np.pi)
ax.set_xlim(-2,2)
ax.set_ylim(0,1)
ax.set_xticks([-2, delta-.5, delta, 2])
ax.set_yticks([0,1],)
ax.set_xticklabels(['$-2$', '$\~\delta-1/2$', '$\~\delta$', '$2$'],{'fontsize':20})
ax.set_yticklabels([0,1],{'fontsize':20})
ax.set_xlabel('$\~\omega$',{'fontsize':20})
ax.set_ylabel('$\~q$',{'fontsize':20})
ax.legend(fontsize = 20)
plt.show()
