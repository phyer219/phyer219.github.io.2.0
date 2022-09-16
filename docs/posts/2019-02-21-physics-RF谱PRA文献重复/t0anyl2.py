import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

l = 1



d = 0



def I(o):

    def I(q):
        g = o - d + q**2/2

        cc = (1+2*g)/(2*q)
        dd = np.sqrt( np.abs(2*g) )/q

        def a(x):
            r1 = q*x + np.sqrt( np.abs(q**2*x**2-2*g) )
            r2 = q*x - np.sqrt( np.abs(q**2*x**2-2*g) )
            a = 1/(r1 -r2) * \
                (\
                  np.heaviside(-g,0) * np.heaviside(cc-x,0) * r1**2 \
                 +np.heaviside( g,0) * np.heaviside(x-dd,0) * np.heaviside(x,0)\
                 *( np.heaviside(cc-x,0)*r1**2 + r2**2 )\
                )
            return a
        A, err = integrate.quad(a, -1, 1)
        A = np.pi*A

        def b(x):
            r1 = q*x + np.sqrt( np.abs(q**2*x**2-2*g) )
            r2 = q*x - np.sqrt( np.abs(q**2*x**2-2*g) )

            cc = (1+2*g)/(2*q)
            dd = np.sqrt( np.abs(2*g) )/q


            noroot = np.heaviside(g,0)*np.heaviside(dd-x,0)                    # no root heaviside
            root = np.heaviside(-g,0) + \
                np.heaviside(g,0)*np.heaviside(x-dd,0)                    # root heaviside

            bnoroot11 = np.arctan( (1-q*x)/np.sqrt(np.abs(2*g-q**2*x**2 ) ) )
            bnoroot12 = np.arctan( ( -q*x)/np.sqrt(np.abs(2*g-q**2*x**2 ) ) )
            bnoroot1 = (-4*g)/ (2*g - q**2*x**2)*(bnoroot11 - bnoroot12)
            bnoroot2 = 2*q*x*np.log( np.abs( (.5-q*x+g)/g ) )
            bnoroot = bnoroot1 + bnoroot2

            broot1 = -2*g/(r1-r2) * np.log( np.abs((r2*(1-r1))/(r1*(1-r2))) )
            broot2 = 2*q*x/(r1-r2) * \
                (r1*np.log( np.abs(1/r1-1) ) - r2*np.log( np.abs(1/r2-1) ) )
            broot = broot1 + broot2

            b = 2 + noroot*bnoroot +root*broot
            return b
        B, err = integrate.quad(b, -.99, .99)

        I = l**2*A / ( (o-l**2*B)**2 + l**4*A**2 ) *q**2
        return I
    I, err = integrate.quad(I, 0.01, .99)
    return I

N = 5
II = I(-.05)
'''
o = np.linspace(-2, 2, N)
II = np.linspace(0, 0, N)
for i in range (N):
    II[i] = I(o[i])
    print(i)
'''
print(II)
