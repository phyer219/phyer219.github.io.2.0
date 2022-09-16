import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
from scipy.special import roots_legendre as leg
def gauquad(f,a,b,n = 50):
    '''
    定义 Gaussian quadrature 积分
    函数 f 的积分区间为 [a,b]
    取 n 个 Legendre 的根
    def Gaussian quadrature integration
    integrate function f from a to b
    take n Legendre roots
    '''
    ft = lambda t: f( (b-a)*t/2 +(a+b)/2 ) * (b-a)/2
    x, w = leg(n)
    I = 0
    for i in range(n):
        I = I + w[i]*ft(x[i])
    err = 0
    return I,err
def twovarplt(f,ax,bx,ay,by,Nx=100,Ny=10,gap = 2):
    '''
    两变量画图
    f(x,y): 要绘制的函数
    变量 x 的取值区间为 [ax,bx], 取点的个数为 Nx 个
    变量 y 的取值区间为 [ay,by], 画 Ny 条线, 每条线对应一个 y 值
    线与线之间的间隔为 gap
    two variables plot
    plot function f(x,y)
    x takes Nx points from 'ax' to 'bx'
    each line corresponds a fixd y, y takes Ny points from 'ay' to 'by'
    the gap between lines is 'gap'
    '''
    x = np.linspace(ax,bx,Nx)
    y = np.linspace(ay,by,Ny)
    fx = np.linspace(0,0,Nx)
    for j in range(Ny):
        for i in range(Nx):
            print('第',j+1,'条线,','第',i+1,'个点,','共',Ny,'条线,','每条线',Nx,'个点.')
            fx[i] = f(x[i],y[j])
        plt.plot(x,fx+j*gap )
    #    plt.plot(x,x*0+y[j],color=(j/Ny,1-j/Ny,j/Ny))
    plt.xlabel(r'$\tilde{\omega}$')
    plt.ylabel(r'$I(\tilde{\omega})$')
    plt.yticks([])
    plt.savefig('./T = 0.jpeg',writer='imagemagick')
    plt.show()

def f(p,m,T):   # Fermi distribution function
    f = 1/(np.exp((p**2-m)/T)+1)
    return f
def theta(x):   # Heaviside theta function
    if x>=0:
        f = 1
    else:
        f = 0
    return f
def delta(x,b = 1e-2):  # Dirac delta function
    b = 1e-2
    f = b/(b**2 + x**2)/np.pi
    return f

T = 1e-6   # Temperature
m = 1   # Chemical potential mu
up = 10 # Integration cut off of 

def A(o,d,k,p): # the unintegrated Imaginary part of self-energy
    x1 = o-d+p**2/2+k**2/2-p*k
    x2 = o-d+p**2/2+k**2/2+p*k
    if x1>0 or x2<0:
        A = 0
    else:
        A = np.pi*p/k*f(p,m,T)
    return A
def AA(o,d,k):  # the integrated Imaginary part of self-energy
    AA, err = gauquad(lambda p:A(o,d,k,p),0,up)
    return AA
def s(o,d,k,p): # the unintegrated Real part of self-energy
    s = f(p,m,T)*p/k*( np.log( np.abs(o-d + (k+p)**2/2) ) - np.log( np.abs(o-d + (k-p)**2/2) ) )
    return s
def S(o,d,k):   # the integrated Real part of self-energy
    S,err = gauquad(lambda p:s(o,d,k,p),0,up)
    return S

def I(o,d,k):   # the unintegrated spectral function
    aa = AA(o,d,k)
    bb = S(o,d,k)
    if aa == 0:
        I = k**2*f(k,m,T)*delta(o-bb,b=1)
    else:
        I = k**2*f(k,m,T)*aa/((o-bb)**2+aa**2)
    return I
def II(o,d):    # the integrated spectral function
    if d>o:
        II,err = integrate.quad(lambda k:I(o,d,k),0,up,epsabs=1.493-2)
    else:
        II, err = integrate.quad(lambda k:I(o,d,k),0,up,epsabs=1.49e-2)
    return II
    
twovarplt(II,-2,2,-8,8,Nx = 1000,Ny=33,gap=3)

#twovarplt(lambda k ,o:S(o,0,k),0,10,0.1,2,Nx = 100,Ny = 25,gap=0)

'''
def A(o,d,k,x):
    g = o-d+k**2/2
    r1 = k*x + np.sqrt( k**2*x**2 -2*g )
    r2 = k*x - np.sqrt( k**2*x**2 -2*g )
    A = theta(-g)*theta(1+2*g-2*k*x)*r1**2*f(r1,m,T)
    A = A+ theta(g)*theta(k*x-np.sqrt(2*g))*theta(x) * ( theta(1+2*g-2*k*x)*r1**2*f(r1,m,T) + r2**2*f(r2,m,T))
    A = A/(r1-r2)
    return A
def AA(o,d,k):
    AA, err = gauquad(lambda x:A(o,d,k,x),-1,1)
    AA = np.nan_to_num(AA)
    AA = np.pi*AA
    return AA
'''
'''
    n = 500
    k = np.linspace(1e-5,up,n)
    for i in range(n):
        dd = np.abs(o - S(o,d,k[i]))
    #    print(dd)
        if dd<1e-1:
            ko = k[i]
            break
        else:
            ko = 0
    II = ko**2*f(ko,m,T)
    return II
'''
