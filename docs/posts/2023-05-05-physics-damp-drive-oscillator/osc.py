import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import quad


def quad_c(func, *args, **kwargs):
    re = quad(lambda x: func(x).real, *args, **kwargs)
    im = quad(lambda x: func(x).imag, *args, **kwargs)
    return re[0]+1j*im[0], re[1]+1j*im[1]


def ftrans(func, x):
    res = quad_c(func, 0, np.inf, weight='cos', wvar=x)[0]
    res += 1j*quad(func, 0, np.inf, weight='sin', wvar=x)[0]
    res += quad(func, -np.inf, 0, weight='cos', wvar=x)[0]
    res += 1j*quad(func, -np.inf, 0, weight='sin', wvar=x)[0]
    return res/np.sqrt(2*np.pi)


class Oscillator:
    def __init__(self, w, Ft, x0, v0):
        """
        dx^2/dt^2 + w^2 = Ft
        w: oemga
        Ft: function of t
        x0: intial position
        v0: intial dx/dt, volecity
        """
        self.w = w
        self.Ft = Ft
        self.x0 = x0
        self.v0 = v0

    def dX_dt(self, X, t):
        return [X[1], -self.w**2*X[0] + self.Ft(t)]

    def xi_im_landau(self, t):
        """
        Imaginary part of Landau (22.10) with out xi_0
        """
        xil = - quad(self.Ft, 0, t,
                     weight='sin', wvar=self.w)[0] * np.cos(self.w*t)
        xil += quad(self.Ft, 0, t,
                    weight='cos', wvar=self.w)[0] * np.sin(self.w*t)
        return xil

    def X_t_ana(self, t, ts):
        xt = self.xi_im_landau(t) / self.w

        xt += np.cos(self.w*t) * self.x0

        dxi_dt0 = self.xi_im_landau(ts[1]) - self.xi_im_landau(ts[0])
        dxi_dt0 /= ts[1] - ts[0]

        xt += np.sin(self.w*t) * (self.v0 - dxi_dt0/self.w) / self.w
        return xt

    def X_t_ana_FT(self, t):
        xt = quad(lambda s: (self.Ft(t+s) + self.Ft(t-s)), 0, np.inf,
                  weight='sin', wvar=self.w)[0]
        xt /= (2*self.w)

        cor = np.sin(self.w*t) * quad(self.Ft, 0, np.inf,
                                      weight='cos', wvar=self.w)[0]
        cor -= np.cos(self.w*t) * quad(self.Ft, 0, np.inf,
                                       weight='sin', wvar=self.w)[0]
        cor -= np.sin(self.w*t) * quad(self.Ft, -np.inf, 0,
                                       weight='cos', wvar=self.w)[0]
        cor += np.cos(self.w*t) * quad(self.Ft, -np.inf, 0, weight='sin',
                                       wvar=self.w)[0]

        xt += cor/(2*self.w)
        xt += np.cos(self.w*t) * self.x0

        dxi_dt0 = self.xi_im_landau(ts[1]) - self.xi_im_landau(ts[0])
        dxi_dt0 /= ts[1] - ts[0]

        xt += np.sin(self.w*t) * (self.v0 - dxi_dt0/self.w) / self.w
        return xt

    def Xt_ode(self, ts):
        Xs = odeint(self.dX_dt, [self.x0, self.v0], ts)
        return Xs


osc = Oscillator(w=.5, Ft=lambda t: 5*np.exp(-(t-10)**2), x0=.7, v0=.5)
ts = np.linspace(0, 30, 300)
plt.plot(ts, [osc.X_t_ana_FT(ti) for ti in ts], 'ro', mfc='None', ms=10,
         label='Fourier')
plt.plot(ts, osc.Xt_ode(ts)[:, 0], 'bx', label="Numerically solve ODE")
plt.plot(ts, [osc.X_t_ana(ti, ts) for ti in ts], 'g', label='Analytic', lw=2)
plt.xlabel('t')
plt.legend()
plt.savefig('osc.png', transparent=True)
plt.show()
