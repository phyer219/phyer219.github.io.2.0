import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches  # 导入这个包来画箭头

myfig = plt.figure(figsize=[8, 4])  # 先建立画板.

excAxes = myfig.add_subplot(121, title='Dispersion')  # 为激发谱添加画纸.
dosAxes = myfig.add_subplot(122, title='Density of States')  # 为态密度添加画纸.

# 隐藏四边的边框, 以及刻度
for ax in [excAxes, dosAxes]:
    ax.spines['top'].set_visible(False) 
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    #ax.grid(True)

lc = 'black'                    # 坐标轴等的颜色

# 画出激发谱的 x 轴, 使用了 matplotlib 包中的箭头. 前两个参量是起点和终点的坐标.
# mutation_scale 表征箭头的大小. lw 是 linewidth.
excX = mpatches.FancyArrowPatch((-.5, 0), (4, 0), mutation_scale=15,
                                 arrowstyle='->', color=lc, lw=1.5) 
excAxes.add_patch(excX)         # 把画出的 x 轴添加到画纸上
# 同样的方法画出 y 轴.
excY = mpatches.FancyArrowPatch((0, -5), (0, 8), mutation_scale=15,
                                 arrowstyle='->', color=lc, lw=1.5) 
excAxes.add_patch(excY)

# 添加一些注释, 全都用了 annotate. xy 表示要注释的位置, xytext 表示注释文字放置
# 的位置. 如果有 arrowprops 参数, 就会添加一个箭头.
excAxes.annotate(r'$k$', xy=(3.5, .2), color=lc)  # x 轴的意义
excAxes.annotate(r'$E(k)$', xy=(.2, 7), color=lc)  # y 轴的意义
excAxes.annotate(r'$0$', xy=(0, 0), xytext=(.1,.2), color=lc)  # 坐标原点

excAxes.annotate(r'$k_F$', xy=(1.7, .2), color=lc)  # 标注化学势的位置
excAxes.annotate(r'Fermi Wave Vector', xy=(2, 0), xytext=(2, -3),
                 arrowprops=dict(arrowstyle='->', color='r'), color='r')

# 对态密度图进行类似的操作
dosX = mpatches.FancyArrowPatch((-.5, 0), (4, 0), mutation_scale=15,
                                 arrowstyle='->', color=lc, lw=1.5) 
dosAxes.add_patch(dosX)
dosY = mpatches.FancyArrowPatch((0, -1), (0, 3), mutation_scale=15,
                                 arrowstyle='->', color=lc, lw=1.5) 
dosAxes.add_patch(dosY)

dosAxes.annotate(r'$E$', xy=(3.5, .1), color=lc)
dosAxes.annotate(r'$D(E)$', xy=(.2, 2.5), color=lc)
dosAxes.annotate(r'$0$', xy=(0, 0), xytext=(.2,.1), color=lc)

dosAxes.annotate(r'$\mu$', xy=(2.1, .1), color=lc)
dosAxes.annotate(r'Fermi Level', xy=(2, 0), xytext=(2, -.8),
                 arrowprops=dict(arrowstyle='->', color='r'), color='r')
dosAxes.plot([2, 2],[0, np.sqrt(2)], '--', c='gray')  # 画出费米面的虚线

# 坐标建立完, 画出相应的曲线
mu = 4
k = np.linspace(0, 3.5, 100)

exline = k**2 - mu
excAxes.plot(k, exline, 'b')
# 注释画出的曲线
excAxes.annotate(r'$\frac{k^2}{2m}-\mu$', xy=(2.3, 6), color='b')


E = np.linspace(0, 3.5, 100)
DOS = np.sqrt(E)
dosAxes.plot(k, DOS, 'b')
# 注释画出的曲线
dosAxes.annotate(r'$\propto \sqrt{E}$', xy=(2.5, 2), color='b')

myfig.savefig('gapless.jpg')    # 保存图片
