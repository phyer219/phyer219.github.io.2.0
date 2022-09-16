import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

l = 1                           # 定义变量

def delta(x):
    b = .01
    f = b/(b**2 + x**2)/np.pi
    return f

def I(o,d):

    def I(x):
        def I(q):
            g = o - d + q**2/2
            case = 1

            if q**2*x**2<2*g:        # 无根
                A = 0
                case = 0
                w = o-d+q*(1-x**2)/2
                B = 1/( w ) * ( \
                                 np.arctan( (1-q*x)/np.sqrt( 2*w )  ) - \
                                 np.arctan( ( -q*x)/np.sqrt( 2*w )  )  )
            else:               # 有根
                r1 = q*x + np.sqrt( q**2*x**2 - 2*g )
                r2 = q*x - np.sqrt( q**2*x**2 - 2*g )
                if r1<1 and r2>0: # 两根都在内
                    A = 2/( r1-r2 ) # 根都在积分区间内
                    B = 1/(r1-r2)*np.log( ( (1-r1)*r2 )/ \
                               ( (1-r2)*r1 ) )
                elif r1<1 or r2>0: # 一内一外
                    A = 1/( r1-r2 ) # 根都在积分区间内
                    B = 1/(r1-r2)*np.log( (-(1-r1)*r2 )/ \
                               ( (1-r2)*r1 ) )
                else:           # 都在外
                    A = 0
                    case = 0
                    B = 1/(r1-r2)*np.log( ( (1-r1)*r2 )/ \
                               ( (1-r2)*r1 ) )

            if case == 0:
                I = delta(o - l**2*B)
            else:
                I = l**2*A / ( (o-l**2*B)**2 + l**4*A**2 )
            return I

        (fres, err) = integrate.quad(I,0,1)

        return fres


    (fres, err) = integrate.quad(I,-1,1)
    return fres


N = 8
#画图的横坐标omega从-2取到2
omega = np.linspace(-2,2,N)

C = 1 # 画C根线
#求出想要的函数在横坐标取值区间内的结果
I_omega = np.linspace(0,0,N)

for j in range (C):
    d = j-(C-1)/2
    d = d/2 #间距是分母分之一
    for i in range(N):
        I_omega[i] = I(omega[i],d)
#        print(d)
#        print(i-1)
    plt.plot(omega,I_omega+j*10, label='d= %.2f' %(d) , color='gray')

plt.show()



'''
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

l = 1                           # 定义变量

def delta(x):
    b = .001
    f = b/(b**2 + x**2)/np.pi
    return f

def I(o,d):
    def I(x):
        def I(q):
            g = o - d + q**2/2

            if q**2*x**2>2*g:   # 有根
                r1 = q*x + np.sqrt( q**2*x**2 - 2*g )
                r2 = q*x - np.sqrt( q**2*x**2 - 2*g )

                a2 = 2/( r1-r2 ) # 根都在积分区间内
                b2 = 1/(r1-r2)*np.log( ( (1-r1)*r2 )/ \
                               ( (1-r2)*r1 ) )

                a3 = 1/( r1 - r2 ) # 一内一外
                b3 = 1/(r1-r2)*np.log(-( (1-r1)*r2 )/ \
                              ( (1-r2)*r1 ) )

                a4 = 0                   # 都在外
                b4 = b2
                if r1<1 and r2>0: # 根都在积分区间内
                    A, B = a2, b2
                    case = 2
                elif r1>1 or r2<0: # 一内一外
                    A, B = a3, b3
                    case = 3
                else:               # 都在外
                    A, B = a4, b4
                    case = 4

            else:
                A = 0                  # 无根
                w = o-d+q*(1-x**2)/2
                B = 1/( w ) * ( \
                                 np.arctan( (1-q*x)/np.sqrt( 2*w )  ) - \
                                 np.arctan( ( -q*x)/np.sqrt( 2*w )  )  )
                case = 1


            if case == 2 or case == 3:
                I = l**2*A / ( (o-l**2*B)**2 + l**4*A**2 )
            else:
                I = delta(o - l**2*B)
            return I
        (fres, err) = integrate.quad(I, 0, 1)
        return fres
    (fres, err) = integrate.quad(I, -1, 1)
    return fres




N = 64
#画图的横坐标omega从-2取到2
omega = np.linspace(-.3,2,N)

C = 1 # 画C根线
#求出想要的函数在横坐标取值区间内的结果
I_omega = np.linspace(0,0,N)

for j in range (C):
    d = j-(C-1)/2
    d = d/2 #间距是分母分之一
    for i in range(N):
        I_omega[i] = I(omega[i],d)
#        print(d)
#        print(i-1)
    plt.plot(omega,I_omega+j*10, label='d= %.2f' %(d) , color='gray')

plt.show()




import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

# 定义变量
l = 1 # lambd_tilde

#画图的精度
N = 10


d = 1
l = 1

# 定义delta函数
def delta(x):
    b = .1
    f = b/(b**2 + x**2)/np.pi
    return f
# 定义主值函数
def pv(x):
    b = 0.1
    f = x/(b*2 + x**2)
    return f

o = .1
def A(p, q, x):
    A = np.pi * p**2 * delta( o - d + p**2/2 + q**2/2 - p*x )
    return A

def B(p, q, x):
    B =         p**2 * pv( o - d + p**2/2 + q**2/2 - p*x )
    return B

I = lambda q, p, x: l**2*A(p,q,x)/( (o - l**2*B(p,q,x))**2 + l**4*A(p,q,x)**2 )
(fress, err) = integrate.tplquad(I,-1,1, lambda x:0, lambda x:1, lambda p, x:0, lambda p, x:1)

b = fress

omega = np.linspace(-2, 2, N)
I_omega = np.linspace(0, 0, N)

print(b)

for i in range(N):
    I_omega[i] = I(omega[i])
    print(i)

plt.plot(o,I)
plt.show()
'''
