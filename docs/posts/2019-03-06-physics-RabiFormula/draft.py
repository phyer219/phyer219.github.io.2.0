import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

N = 1000

gamma = 1

t = np.linspace(0,16,N)

def c2(omega):
    Omega = np.sqrt( (omega-1)**2/4 + gamma )
    c2 = 1/( 1+(omega-1)**2/(4*gamma**2) ) \
        *np.sin(Omega*t)**2
    ax.set_xticks([np.pi/Omega, 2*np.pi/Omega, \
                   3*np.pi/Omega, 4*np.pi/Omega, \
                   5*np.pi/Omega])
    ax.set_xlim(0,4*np.pi/Omega)
    return c2

fig, ax = plt.subplots()
line, = ax.plot(t,c2(1))

#ax3 = fig.add_axes([0.1, 0.1, 0.8, 0.8])



def init():
    line.set_ydata(c2(1))
    return line

def animata(i):
    line.set_ydata(c2(1+.01*i))
#    ax.text(1+0.1*i,1,'x')
    return line

ani = animation.FuncAnimation(fig=fig, func=animata, \
                              frames=400, interval=20)

ax.set_xlabel('$t$')
ax.set_ylabel('$|c_2(t)|^2$')
ax.set_title('Plot of $|c_2(t)|^2$ at $\omega = \omega_{21}$ to $\omega =5 \omega_{21}$')

ax.set_yticks([0,0.2,0.5,1])

ax.set_xticklabels(['$\pi/\Omega$', '$2\pi/\Omega$', \
                    '$3\pi/\Omega$', '$4\pi/\Omega$', \
                    '$5\pi/\Omega$'])
ani.save('fig.gif',writer='imagemagick')
plt.show()
