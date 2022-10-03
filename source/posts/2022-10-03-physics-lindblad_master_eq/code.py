import numpy as np
import matplotlib.pyplot as plt


def hamiltonian(N, gamma_l, gamma_r):
    a = np.eye(N-1)
    right = np.vstack((np.zeros(N-1), a))
    right = np.hstack((right, np.zeros([N, 1])))
    left = np.hstack((np.zeros([N-1, 1]), a))
    left = np.vstack((left, np.zeros(N)))
    pbc = np.zeros([N, N])
    pbc[0, -1] = gamma_l        # peridical boundary condition
    pbc[-1, 0] = gamma_r
    h = left*gamma_l + right*gamma_r + pbc
    return h


N = 10
h = hamiltonian(N, 1, 2)
plt.imshow(h)
plt.colorbar()
plt.savefig('hamiltonian.png', transparent=True)

P = np.array([[np.exp(-1j*2*np.pi/N * a*b) for a in range(N)]
              for b in range(N)])
D = P.conjugate()@h@P
plt.clf()
plt.imshow(np.abs(D))
plt.colorbar()
plt.savefig('population.png', transparent=True)

eigenvalues = np.array([D[i, i] for i in range(N)])
plt.clf()
for i in eigenvalues:
    plt.plot(i.real, i.imag, 'bo')
plt.xlabel('Re')
plt.ylabel('Im')
plt.savefig('eigenvalues.png', transparent=True)
