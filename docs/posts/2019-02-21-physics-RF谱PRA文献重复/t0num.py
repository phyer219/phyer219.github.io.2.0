import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

# 定义变量
l = 1 # lambd_tilde

#画图的精度
N = 100

# 定义delta函数
def delta(x):
    b = .0001
    f = b/(b**2 + x**2)/np.pi
    return f
# 定义主值函数
def pv(x):
    b = 0.0001
    f = x/(b*2 + x**2)
    return f


# 定义最终想要得到的函数
def I(o,d):

    def I(q):#定义没有积分的结果

        def A(q):#定义theta的虚部
            def A(p):
                def A(x):
                    y = o + p**2/2 + q**2/2 -p*x - d
                    A =p**2*np.pi * delta(y)
                    return A
                (fres,err) = integrate.quad(A,-1,1)
                return fres
            (fres,err) = integrate.quad(A,0,1)
            return fres

        def B(q):#定义theta的实部
            def B(p):
                def B(x):
                    y = o + p**2/2 + q**2/2 -p*x - d
                    B = p**2*pv(y)
                    return B
                (fres,err) = integrate.quad(B,-1,1)
                return fres
            (fres,err) = integrate.quad(B,0,1)
            return fres

        I =q**2* l**2*A(q) / ( (o-l**2*B(q))**2 + l**4*A(q)**2 )
        return I

    (fres,err) = integrate.quad(I,0,1)#对其积分,即得到最终结果
    return(fres)



#画图的横坐标omega从-2取到2
omega = np.linspace(-2,2,N)

C = 3# 画C根线
#求出想要的函数在横坐标取值区间内的结果
I_omega = np.linspace(0,0,N)

for j in range (C):
    d = j-(C-1)/2
    d = d/2 #间距是分母分之一
    for i in range(N):
        I_omega[i-1] = I(omega[i-1],d)
        print(d)
        print(i-1)
    plt.plot(omega,I_omega+100*j, label='d= %.2f' %(d) , color='gray')

#plt.legend()

plt.show()
