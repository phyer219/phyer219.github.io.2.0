import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.special import hermite
import math


# x = np.linspace(-3, 3)
# check hermite polynomials
# plt.plot(x, hermite(3)(x))
# plt.plot(x, 8*x**3 - 12*x, 'x')


def ho_eig(x, n, m=1, o=1):
    """harmonic oscillator eigenfunctions and eigenvalues"""
    psi = 1 / np.sqrt(2**n * math.factorial(n))
    psi *= (m*o / np.pi)**(1/4)
    psi *= np.exp(-m*o * x**2 / 2)
    psi *= hermite(n)(np.sqrt(m*o) * x)
    energy = (n + 1/2) * o
    return energy, psi


# check ho_eig
# x = np.linspace(-10, 10, 1000)
# plt.plot(x, ho_eig(x, 3)[1])
# integrate.quad(lambda x:(ho_eig(x, 3)[1])**2,-10, 10)


def Mehler_kernel(x, tau, x0=0, m=1, o=1):
    """propagator of 1D harmonic oscillator, also known as Mehler kernel"""
    K = np.sqrt(m*o/2/np.pi/np.sinh(o*tau))
    K *= np.exp(-(m*o*(x**2 + x0**2)*np.cosh(o*tau) - 2*x*x0)/2/np.sinh(o*tau))
    return K


# check Mehler_kernel
# x = np.linspace(-10, 10, 1000)
# for ti in [0.1, 1, 2]:
#     plt.plot(x, Mehler_kernel(x, tau=ti))
#     print(integrate.quad(lambda x:Mehler_kernel(x, tau=0.1), -5, 5))


def HO_propagator(x, tau, x0=0, m=1, o=1, cut=15):
    """1D harmonic oscillator propagator, by eigenfunction expansion"""
    p = 0
    for n in range(cut):
        energy, psi = ho_eig(x, n)
        _, psi0 = ho_eig(x0, n)
        p += np.exp(-energy*tau) * psi * psi0
    return p


# compare the results of 1D harmonic oscillator propagator given by two methods
x = np.linspace(-5, 5, 1000)
for ti in [0.1, 1, 3]:
    p = plt.plot(x, Mehler_kernel(x, tau=ti), lw=2,
                 label=rf'$\tau\omega={ti}$')
    plt.plot(x[::10], HO_propagator(x, tau=ti)[::10], lw=0,
             marker='o', mec=p[0].get_color(), ms=5, mfc='none')
    print(integrate.quad(lambda x:Mehler_kernel(x, tau=0.1), -5, 5))
plt.title(r'$K(x, \tau; 0, 0)$')
plt.xlabel(r'$x/\sqrt{\hbar/(m\omega)}$')
plt.legend()
plt.savefig('HO_propagator.svg', transparent=True)
