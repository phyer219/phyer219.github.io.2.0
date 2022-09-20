import numpy as np
from matplotlib import pyplot as plt

N = 1000

V = np.linspace(0,5,N)
a = 1 - np.tan( np.sqrt(V) )/np.sqrt(V)
a[np.abs(a)>20] = np.inf
Eb = -1/(np.sqrt(a))**4
#Eb[np.abs(Eb)>.3] = np.inf
'''
Et = np.linspace(-5,5,N)
Vt = np.linspace(0, 40,N)
Et, Vt = np.meshgrid(Et, Vt)
ax.contour(Vt,Et,Vt**2+Et**2,levels=[3])
'''

#Eb[int(1.6*N/3):] = np.inf

fig, ax = plt.subplots()
ax.set_ylim(-10,10)
ax.plot(V,a,label='Scattering Length')
ax.plot(V,Eb,label='Shallow bound State Energy')

ax.set_xticks([0,(np.pi/2)**2])
ax.set_xticklabels([r'$0$', r'$\left(\frac{\pi}{2}\right)^2$'])

ax.set_yticks([-5,0,5])
ax.set_yticklabels([r'$-5$', r'$0$',r'$5$'])


ax.set_xlabel(r'$V_0/\frac{\hbar^2}{2\mu r_0^2}$')
ax.set_ylabel(r'$a_s/r_0$')
ax.legend()
ax.set_title(r'Scattering length and shallow bound state energy VS well depth')

plt.show()

'''
N = 1000

E = np.linspace(-5,5,N)
V = np.linspace(0, 40,N)
E, V = np.meshgrid(E, V)

L = np.sqrt(-E)
R = -np.sqrt(E+V)/np.tan(np.sqrt(E+V))
Z = L-R
Z[np.abs(Z)>20] = np.inf
plt.contour(V, E,Z,levels=[0])

a = 1-np.tan( np.sqrt(V) )/np.sqrt(V)
a[np.abs(a)>100] =np.inf
plt.plot(V,a,'r',linewidth = 1)
plt.ylim(-2,2)

plt.plot(V,0*V,linewidth=1)

plt.show()
'''
