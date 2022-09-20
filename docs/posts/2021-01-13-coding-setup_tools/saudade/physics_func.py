import numpy as np

def ts(f, a, b, n=51):
    """Tanh-sinh quadrature 方法. 适用于端点发散的情况."""
    up = 4
    h = 2*up / (n-1)
    t = np.linspace(-up, up, n, endpoint=True)
    x = np.tanh(1/2*np.pi*np.sinh(t))
    w = 1/2*h*np.pi*np.cosh(t)
    w = w/(np.cosh(1/2*np.pi*np.sinh(t))**2)
    gc = 0
    for i in range(n):
        p = (x[i]*(b-a) + a + b)/2
        gc = gc + f(p)*w[i]
    err = 0
    gc = gc * (b-a)/2
    return gc, err

def bose(beta, energy):
    """Bose 分布函数"""
    x = -beta * energy
    return np.exp(x) / (1 - np.exp(x))

def cos_theta_kq(theta_k, phi_k, theta_q, phi_q):
    """k, q 夹角的余弦值"""
    x = (np.sin(theta_k)*np.sin(theta_q) * np.cos(phi_k - phi_q) 
            + np.cos(theta_k)*np.cos(theta_q))
    return x

class PrincipalValueInt():
    """分母带有无穷小的那种积分"""
    def __init__(self, numerator, coeff, down_bound, upbound):
        """初始化, numerator 都是函数. 分母为 a*x**2 + b*x + c"""
        self.numerator = numerator
        self.down_bound = down_bound
        self.upbound = upbound
        self.coeff = coeff
        a = coeff[0]
        b = coeff[1]
        c = coeff[2]
        self.delta = b**2 - 4*a*c

    def get_imag(self):
        """计算积分的虚部."""
        root_exist = self.delta > 0

        if root_exist:
            # 如果根存在, 计算两根
            root1 = (-self.coeff[1] - np.sqrt(self.delta)) / (2 * self.coeff[0])
            root2 = (-self.coeff[1] + np.sqrt(self.delta)) / (2 * self.coeff[0])

            # 判断两根是否位于积分区间内
            root1_in = self.down_bound < root1 and root1 < self.upbound
            root2_in = self.down_bound < root2 and root2 < self.upbound

            # 计算积分结果
            imag = (root1_in) * self.numerator(root1) 
            imag += (root2_in) * self.numerator(root2) 
            imag *= -np.pi / np.abs(root2 - root1)
        else:
            # 根不存在, 虚部为 0
            imag = 0 
        imag *= 1/self.coeff[0] # bug No.2 分子要除以 a 才行.
        return imag