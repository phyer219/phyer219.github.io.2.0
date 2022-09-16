import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches  # 导入这个包来画箭头

myfig = plt.figure(figsize=[8, 6])
ax = myfig.add_subplot(111)

# 隐藏边框
[ax.spines[i].set_visible(False) for i in ['top', 'right', 'left', 'bottom']]
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0.25, 2)
ax.set_ylim(0.5, 4)

ax.plot([1, 2], [1, 1], 'r', lw=5)
ax.plot([1, 2], [2, 2], 'r', lw=5)
ax.plot([1, 2], [3, 3], 'g', lw=5)
ax.annotate(r'$|1\rangle$', xy=(1, 1), xytext=(.8, .9), fontsize=30, color='r')
ax.annotate(r'$|2\rangle$', xy=(1, 2), xytext=(.8, 1.9), fontsize=30, color='r')
ax.annotate(r'$|3\rangle$', xy=(1, 3), xytext=(.8, 2.9), fontsize=30, color='g')

ax.annotate('superfluid \n pairing', xy=(.75, 1), xytext=(.25, 1.3),
            arrowprops=dict(arrowstyle='<-', lw=2, color='r'), fontsize=15,
            color='r') 
ax.annotate('', xy=(.75, 2), xytext=(.6, 1.5), arrowprops=dict(arrowstyle='<-',
            lw=2, color='r'), fontsize=15, color='r')
ax.annotate('effectively free atom excitation levle\n unoccupied intially',
            xy=(1, 3.3), xytext=(1, 3.8), arrowprops=dict(arrowstyle='<-', lw=2,
                                                          color='g'),
            fontsize=15, color='g')

ax.annotate(r'$^6\mathrm{Li}$', xy=(.3, 3.8), fontsize=40, color='b')

rf = mpatches.FancyArrowPatch((1.25, 2), (1.25, 3), mutation_scale=15,
                              arrowstyle='<->', color='orange', lw=2)
ax.add_patch(rf)
ax.annotate('rf field', xy=(1.3, 2.5), fontsize=15, color='orange')

myfig.savefig('level.jpg')    # 保存图片
