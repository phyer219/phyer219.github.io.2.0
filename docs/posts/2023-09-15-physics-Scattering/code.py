import numpy as np
import matplotlib.pyplot as plt


class RectangularPotentialScattering:
    """Rectangular potential barrier"""
    def __init__(self, E, V0, a):
        self.E = E
        self.V0 = V0
        self.a = a

        self.k = np.sqrt(2*E)
        self.K = np.sqrt(2*(V0-E))

    def S(self):
        """0<E<V0"""
        S_val = -2j*self.k/self.K
        S_val /= ((1 - (self.k/self.K)**2) * np.sinh(self.K*self.a)
                   - 2j*self.k/self.K*np.cosh(self.K*self.a))
        S_val *= np.exp(-1j*self.k*self.a)
        return S_val

    def R(self):
        """0<E<V0"""
        R_val = self.S() * (1+1j*self.k/self.K) * np.exp(1j*self.k*self.a
                                                         self.K*self.a)
        R_val -= 1+1j*self.k/self.K
        R_val /= 1-1j*self.k/self.K
        return R_val

def f_kk(E, V0, a):
    return (S(E, V0, a)-1)*2*np.pi/1j

def f_mkk(E, V0, a):
    return R(E, V0, a)*2*np.pi*1j

def sigma_total(E, V0, a):
    k = np.sqrt(2*E)
    return (np.abs(f_kk(E, V0, a))**2 + np.abs(f_mkk(E, V0, a))**2)/k

def sigma_total_optical_theorems(E, V0, a):
    k = np.sqrt(2*E)
    return 4*np.pi*f_kk(E, V0, a).imag/k

a = 0.2
V0 = 5
Es = np.linspace(1e-2, V0, 100, endpoint=False)
Ss = []
Rs = []
sigma_total_s = []
optical_theorem_s = []
sigma_kk_s = []
sigma_mkk_s = []
f_kk_s = []
f_mkk_s = []
for ei in Es:
    Ss.append(S(ei, V0, a))
    Rs.append(R(ei, V0, a))
    sigma_total_s.append(sigma_total(ei, V0, a))
    optical_theorem_s.append(sigma_total_optical_theorems(ei, V0, a))
    sigma_kk_s.append(np.abs(f_kk(ei, V0, a))**2/np.sqrt(2*ei))
    sigma_mkk_s.append(np.abs(f_mkk(ei, V0, a))**2/np.sqrt(2*ei))
    f_kk_s.append(f_kk(ei, V0, a))
    f_mkk_s.append(f_mkk(ei, V0, a))
    
plt.plot(Es, np.abs(Ss)**2, label=r'$|S|^2$')
plt.plot(Es, np.abs(Rs)**2, label=r'$|R|^2$')
plt.plot(Es, ((np.array(Rs).conjugate())*np.array(Ss) - np.array(Rs)*(np.array(Ss).conjugate())).real, 'x')
plt.xlabel('in coming energy E')
plt.legend()
plt.savefig('fig.png', transparent=True)
