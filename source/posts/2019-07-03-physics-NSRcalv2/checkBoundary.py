from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate

from scipy.integrate import fixed_quad
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

rootNum = 10                    # Gaussian Quadrature 积分时取的根的个
                                # 数.
beta = 100                      # 温度的倒数.
er = 1e-6                       # 积分从零开始时, 为避免发散, 从一个非
                                # 常小的数值开始积.
R = 1/30                        # 参数 k_epsilon R 的取值.
epsabs = 1e-1                   # 用 integrate.quad 积分时限定的绝对误
                                # 差 .

#定义用到的函数.
def xi(k, mu):
    return k**2 - mu
def n(k, mu):
    x = xi(k,mu)
    n =  1 / (np.exp(beta*x) - 1)
    return n
def z(omega, q, mu):
    return omega - q**2/2 + 2*mu
 

def pi(omega, q, k, mu):
    """没有积分时的 PI"""
    pi = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
    pi = pi / (2*k**2 - z(omega, q, mu))
    pi = pi * k**4
    pi = pi -k**2/2 - z(omega, q, mu)/4
    pi = 2*pi / np.pi**2 * R
    return pi

def PI(omega, q, mu):
    """将函数 pi 中的 k 积分掉"""
    zz = z(omega, q, mu)
    if zz<0:
        PI, err = fixed_quad(lambda x: pi(omega, q, x, mu), er, 10,
                             n=rootNum)
        # 积分范围是 [0, inf], 如果 z<0 , 在积分范围内分母没有零点, 直
        # 接积分即可.
    else:
        # 如果在积分范围内出现了零点, 就需要考虑它的主值积分.
        # 可以求得在积分范围内的零点为:
        a = np.sqrt(zz/2)
        # 在零点两侧分别积分, 然后相加.
        PI1, err = fixed_quad(lambda x: pi(omega, q, x, mu), er, a-er,
                              n=rootNum) 
        PI2, err = fixed_quad(lambda x: pi(omega, q, x, mu), a+er,
                              10, n=rootNum)
        PI = PI1 + PI2
    return PI

def delta(omega, q, rkv, mu):
    """函数 delta^p"""
    zz = z(omega, q, mu)
    if zz<0:
        # 如果 z<0 , 它是没有虚部的.
        img = 0
    else:
        # 否则, 主值积分后会有一个虚部, 解析表达式为.
        k = np.sqrt(zz/2)
        img = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
        img = img * R/(2*np.pi)
        img = img * k**3
    # delta 实部就是 PI 的实部再加上两项.
    rel = PI(omega, q, mu)
    rel = rel + rkv/(4*np.pi)
    rel = rel +zz/(4*np.pi)
    # delta 取其辐角. 为了使最后的积分收敛, 整体做一个 pi 相位的调整.
    delta = np.angle(rel + 1j*img) - np.pi
    return delta


# 接下来比较数值上得到的 delta 和 近似的解析表达式是否一致.
# delta 是 omega 和 q 两个变量的函数. 最终画图时以 q 为横坐标, 以
# omega 为纵坐标.
N = 100                         # 横坐标取 N 份.
M = 100                         # 纵坐标取 M 份.
mu = -.5                        # 化学势 mu 的取值.
rkv = 1                         # 参数 2R/(kv) 的取值.

# q 和 omega 的取值范围.
q = np.linspace(-4, 4, N)
omega = np.linspace(-1, 8, M)

#将数值计算得到的 delta 保存在变量 numDelta 中.
numDelta = np.zeros(N*M)
numDelta.shape = (M, N)
for i in range(M):
    for j in range(N):
        numDelta[i, j] = delta(omega[i], q[j], rkv, mu)

# 将每一个横坐标对应的 delta 突变的纵坐标保存在变量 step 中
step = np.zeros(N)
for i in range(M-1):
    for j in range(N):
        if numDelta[i, j]>-1 and numDelta[i+1, j]<-3:
            step[j] = i
y = np.zeros(N)
for i in range(N):
    stepi = int(step[i])
    y[i] = omega[stepi]

# 画出数值结果
plt.plot(q, y, 'r', label=r'numerical $\delta^p$ step line')

# 画出解析结果
anaDelta = q**2/2 - 2*mu -rkv
plt.plot(q, anaDelta, 'b', label=r'analytical $\delta^p$ step line')

plt.legend()
plt.xlabel(r'$\tilde{q}$')
plt.ylabel(r'$\tilde{\omega}$')
plt.show()

q, omega = np.meshgrid(q, omega)
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(omega, q, numDelta, cmap=cm.rainbow)

plt.show()
