import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

l = 1                           # 定义变量

def delta(x):
    b = .01
    f = b/(b**2 + x**2)/np.pi
    return f

def I(o,d):
    def I(q):
        r1 = q + np.sqrt( 2*(d-o) )
        r2 = q - np.sqrt( 2*(d-o) )

        a1 = 0                  # 无根
        b1 = 1/(o-d) * ( \
                         np.arctan( (1-q)/np.sqrt( 2*(o-d) )  ) - \
                         np.arctan( ( -q)/np.sqrt( 2*(o-d) )  ))

        a2 = 1/np.sqrt( 2*(d-o) ) # 根都在积分区间内
        b2 = 1/(r1-r2)*np.log( ( (1-r1)*r2 )/ \
                               ( (1-r2)*r1 ) )

        a3 = .5/np.sqrt( 2*(d-o) ) # 一内一外
        b3 = 1/(r1-r2)*np.log(-( (1-r1)*r2 )/ \
                               ( (1-r2)*r1 ) )

        a4 = 0                   # 都在外
        b4 = b2

        if o>d:
            A, B = a1, b1
            case = 1
        elif o>(d-q**2/2) and o>(d-(1-q)**2/2):
            A, B = a2, b2
            case = 2
        elif o>(d-q**2/2) or o>(d-(1-q)**2/2):
            A, B = a3, b3
            case = 3
        else:
            A, B = a4, b4
            case = 4

        if case == 2 or case == 3:
            I = l**2*A / ( (o-l**2*B)**2 + l**4*A**2 )
        else:
            I = delta(o - l**2*B)
        return I
    (fres, err) = integrate.quad(I, 0, 1)
    return fres




N = 1000
#画图的横坐标omega从-2取到2
omega = np.linspace(-2,2,N)

C = 33 # 画C根线
#求出想要的函数在横坐标取值区间内的结果
I_omega = np.linspace(0,0,N)

for j in range (C):
    d = j-(C-1)/2
    d = d/2 #间距是分母分之一
    for i in range(N):
        I_omega[i-1] = I(omega[i-1],d)
        print(d)
        print(i-1)
    plt.plot(omega,I_omega+j*10, label='d= %.2f' %(d) , color='gray')


plt.show()
