import numpy as np
#import matplotlib.pyplot as plt
import functools
import time

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
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def get_data(parameters, func, x):
    '''
    计算画图所需要的点, 并将参数和结果保存到文件.
    由于自己写的这些函数不能输入数组然后输出数组, 所以只能用循环一个一个算
    '''
    num_points = len(x)
    y = []
    pm = parameters.get_parameters()

    # 计算每一个数据点
    for i in range(num_points):
        print(f"正在计算第 {i+1:d}/{num_points:d}个点...")
        yi = func(x[i])
        y.append(yi)

    # 保存数据和参数到文件
    np.savetxt('./data/x.csv', x, delimiter=',')
    np.savetxt('./data/y.csv', y, delimiter=',')
    np.savetxt('./data/paramaters.csv', pm, delimiter=',')
    return x, y, pm


