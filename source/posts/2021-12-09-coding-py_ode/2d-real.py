import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint


def dX_dt(X, t, mu=5):
    return [X[1], mu*(1 - X[0]**2)*X[1] - X[0]]


ts = np.linspace(0, 30, 1000)
X0 = [0, 0.1]
Xs = odeint(dX_dt, X0, ts)


fig, ax = plt.subplots()
line1, = ax.plot(Xs[0, 0], Xs[0, 1], 'o')
line2, = ax.plot(Xs[0, 0], Xs[0, 1], '-')
time_tags = ax.text(-1.5, 4, r'$t = 0$', fontsize=20)


def ani(i):
    line1.set_data(Xs[i, 0], Xs[i, 1])
    line2.set_data(Xs[:i, 0], Xs[:i, 1])
    time_tags.set_text(r'$t=$' + f'{i:n}')
    return None


ax.set_xlim(min(Xs[:, 0]), max(Xs[:, 0]))
ax.set_ylim(min(Xs[:, 1]), max(Xs[:, 1]))
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$x\prime(t)$')
anifig = animation.FuncAnimation(fig=fig, func=ani, frames=len(Xs),
                                 interval=.1)
ax.grid()
anifig.save('2d-real.gif', writer='imagemagick')
