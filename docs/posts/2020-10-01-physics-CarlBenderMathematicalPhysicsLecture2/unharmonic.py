import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig, ax = plt.subplots()

x = np.linspace(-5, 5)

y = lambda epsilon: x**2 + epsilon*x**4

epsilon = -np.linspace(-.1, .1, 200)
ln, = ax.plot(x, y(epsilon[0]))
ax.set_ylim(-1, 10)
text = ax.text(-1, 8, f"$\epsilon={epsilon[0]:.3f}$", fontsize=20, color='red')
ax.set_title(r'$y = x^2 + \epsilon x^4$')

def update(i):
    ln.set_data(x, y(epsilon[i]) )
    text.set_text(f"$\epsilon={epsilon[i]:.3f}$")
    return ln,

my_ani = ani.FuncAnimation(fig=fig, func=update, frames=200, interval=10)

my_ani.save('unharmonic.gif', writer='imagemagick')
plt.show()
