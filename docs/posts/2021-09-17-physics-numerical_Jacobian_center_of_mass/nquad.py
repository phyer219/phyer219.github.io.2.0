from scipy.integrate import nquad


def func(x, y):
    return x**2 + y


def range_x(y):
    return [0, y]


# 先积 x (y, 1), 再积 y(0, 1)
res = nquad(func, [range_x, [0, 1]])
print(res)
print(5/12)
