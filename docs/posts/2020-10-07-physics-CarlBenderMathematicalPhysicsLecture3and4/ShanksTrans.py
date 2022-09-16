import numpy as np
import matplotlib.pyplot as plt

# 计算求和的前 n 项
n=7                             
x = np.linspace(1, n, n)
y = np.zeros(n)
y[0] = 1
for i in range(n-1):
    y[i+1] = y[i] + (-1)**(i+1) * 1/(i+2) 

# 进行 Shanks transform
def shanks_trans(y):
    """Shanks transform"""
    n = y.shape[0]
    # 计算了求和的前 n 项, 最多可做 order 次 Shanks transform
    order = int(np.floor((n - 1) / 2)) 
    st = np.full((order+1, n), np.NaN) 
    st[0] = y
    for i in range(order):
        i += 1
        for j in range(n - 2*i):
            j += i
            st[i, j] = ((st[i-1, j]**2 - st[i-1, j+1]*st[i-1, j-1])
                       /(2*st[i-1, j] - st[i-1, j-1] - st[i-1, j+1]))
    return st
st = shanks_trans(y)

# 画图
for i in range(st.shape[0]):
    plt.plot(x, st[i], 'o', label=f'N = {i:.0f}')
plt.plot(x, x*0+np.log(2), label=f'$\ln 2$')
plt.title('after N  times Shanks transform')
plt.legend()
plt.savefig('ShanksTrans.jpg')
plt.show()
