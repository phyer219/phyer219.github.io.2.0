import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

def delta(x):
    b = .0001
    f = b/(b**2 + x**2)/np.pi
    return f

o = .1
d = 0
l = 1


def I(o)
def I(k):
    def s(p):
        s = p/k *( np.log( np.abs(o-d+ (k+p)**2/2 ) )\
        - np.log( np.abs(o-d+ (k+p)**2/2 ) ))
        return s
    S, err = integrate.quad(s,0,1)
    I = k**2 * delta(o-l**2*S)
    return I

I, err = integrate.quad(I,0,1)
