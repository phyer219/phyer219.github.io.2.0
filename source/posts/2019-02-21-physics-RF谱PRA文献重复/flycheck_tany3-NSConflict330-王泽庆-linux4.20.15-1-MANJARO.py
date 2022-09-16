import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

def delta(x):
    b = .01
    f = b/(b**2 + x**2)/np.pi
    return f
def f(x,T):
    T =5
    f = 1/( np.exp(x/T)+1 )

d = 8
l = 1

T = 5
m = 5

N = 100

def I(o):
    def I(k):
        def s(p):
            s = f(p**2-m) * p/k *( np.log( np.abs(o-d+ (k+p)**2/2 ) )\
            - np.log( np.abs(o-d+ (k-p)**2/2 ) ))
            return s
        S, err = integrate.quad(s,0,1)
        I = f(k**2-m) * k**2 * delta(o-l**2*S)
        return I

    I, err = integrate.quad(I,0,1)
    return I

o = np.linspace(-2,2,N)
Io = np.linspace(0,0,N)
for i in range(N):
    Io[i] = I(o[i])
    print(i)

plt.plot(o,Io)
plt.show()
