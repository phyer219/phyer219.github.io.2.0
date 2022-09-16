import multiprocessing as mp
import time
import functools
import numpy as np
import matplotlib.pyplot as plt

def timer(func):
    """
    Print the runtime of the decorated function.
    参考自: https://realpython.com/primer-on-python-decorators/
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.14f} secs")
        return value
    return wrapper_timer


def foo(x):
    '''
    测试函数, 简单地计算 sin(x), 重复 1e5 次
    '''
    for i in range(int(1e5)):
        a = np.sin(x)    
    a = np.sin(x)
    return a

n = int(96)
x = np.linspace(0, 10, n)

@timer
def loop_single_processing(x, n):
    y_l_s_p = np.zeros(n)
    for i in range(n):
        # 单核运行 n 次 foo(x) 函数
        y_l_s_p[i] = foo(x[i])
    y_l_s_p = foo(x)
    return y_l_s_p

@timer
def loop_multi_processing(x, n):
    pool = mp.Pool()
    y_m_s_p = pool.map(foo, x)
    pool.close()
    pool.join()
    return np.array(y_m_s_p)
    

lsp = loop_single_processing(x, n)
lmp = loop_multi_processing(x, n)

plt.plot(x, lsp, '.', label='loop single processing')
plt.plot(x, lmp+1, '.', label='loop multi processing')
plt.legend()
plt.savefig('fig.png')
plt.show()
