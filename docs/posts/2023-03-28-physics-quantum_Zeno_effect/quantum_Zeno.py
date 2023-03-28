import qutip as qtp
import matplotlib.pyplot as plt
import numpy as np


def num_pe(tlist, tau, rho0=qtp.fock_dm(2, 0)):
    res = qtp.mesolve(H=-1/2*qtp.sigmax(), rho0=rho0, tlist=tlist,
                      c_ops=1/np.sqrt(tau)*qtp.sigmaz(),
                      e_ops=qtp.fock_dm(2, 0))
    return res.expect[0]


def ana_pe(t, tau):
    if tau > 1:
        nu = np.sqrt(1 - 1/tau**2)
        s3 = (np.cos(nu*t) + np.sin(nu*t)/(nu*tau)) * np.exp(-t/tau)
    else:
        mu1 = 1/tau + np.sqrt(1/tau**2 - 1)
        mu2 = 1/tau - np.sqrt(1/tau**2 - 1)
        s3 = (mu2*np.exp(-mu1*t) - mu1*np.exp(-mu2*t)) / (mu2-mu1)
    return (1+s3) / 2


tau = .1
tlist = np.linspace(0, 20, 5000)
plt.plot(tlist, ana_pe(tlist, tau=.5), label=r'Analysis: $\Omega\tau=0.5$',
         ls='-', color='red')
plt.plot(tlist, num_pe(tlist, tau=.5), label=r'Numerical: $\Omega\tau=0.5$',
         ls='-.', lw=3, color='red')
plt.plot(tlist, ana_pe(tlist, tau=10), label=r'Analysis: $\Omega\tau=10$',
         ls='-', color='green')
plt.plot(tlist, num_pe(tlist, tau=10), label=r'Numerical: $\Omega\tau=10$',
         ls='-.', lw=3, color='green')
plt.plot(tlist, ana_pe(tlist, tau=.01), label=r'Analysis: $\Omega\tau=0.01$',
         ls='-', color='blue')
plt.plot(tlist, num_pe(tlist, tau=.01), label=r'Numerical: $\Omega\tau=0.01$',
         ls='-.', lw=3, color='blue')
plt.xlabel(r'$\Omega t$')
plt.ylabel(r'$p_e$')
plt.legend()
plt.savefig('quantum_Zeno.png', transparent=True)
