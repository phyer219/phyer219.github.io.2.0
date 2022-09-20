import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

myfig = plt.figure(figsize=(10, 5))
ax = myfig.add_subplot(111)

[ax.spines[i].set_visible(False) for i in ['left', 'right', 'top', 'bottom']]
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1.5)


N = 100                         # 图片的精细度
lc = 'black'                    # line color

# 画出 D, 也就是图的左边
Da = -1                         # D 图在 x 轴方向的边界
Db = 0
D = np.linspace(Da, Db, N)
ax.scatter([Da, Db], [0, 0], c=lc)  # 画出端点
Dup = np.sin(D*np.pi)               # 上半边的函数
Ddown = np.sin(D*np.pi + np.pi)     # 下半边的函数
ax.plot(D, Dup, c=lc)
ax.plot(D, Ddown, c=lc)
# 打上阴影
div = 10
sl = 'gray'                     # shadow color
for i in range(int(N/div - 2)):
    x1 = D[i*div]
    x2 = D[(i+2)*div]
    y1 = Dup[i*div]
    y2 = Ddown[(i+2)*div]
    ax.plot([x1, x2], [y1, y2], c=sl)
# 标注 D 
ax.annotate(r'$D_0(\mathrm{i}\Omega_m, \vec{0})$', xy=(-1.8, 0), fontsize=20)  
ax.annotate('=', xy=(.15, -.15), fontsize=40)  # 画出等号
    
# 同样的方法画出 G, 也就是图的右边
Ga = .5
Gb = 1.5
G = np.linspace(Ga, Gb, N)
Gup = np.sin(G*np.pi + 3*np.pi/2)
Gdown = np.sin(G*np.pi + np.pi/2)
ax.plot(G, Gup, c=lc, lw=4)
ax.plot(G, Gdown, c=lc)
# 添加两个箭头
ax.scatter([Ga, Gb], [0, 0], c=lc)
arrowup = mpatches.FancyArrowPatch(((Ga+Gb)/2-.05, 1), ((Ga+Gb)/2+.05, 1),
                                   mutation_scale=30, facecolor=lc,
                                   arrowstyle='<-', lw=4)
ax.add_patch(arrowup)

arrowdown = mpatches.FancyArrowPatch(((Ga+Gb)/2-.05, -1), ((Ga+Gb)/2+.05, -1),
                                   mutation_scale=30, facecolor=lc,
                                     arrowstyle='->', lw=1.5)
ax.add_patch(arrowdown)

# 标注两个 G 线
ax.annotate(r'$3, (\mathrm{i}\Omega_m + \mathrm{i}\omega_n, \vec{k})$', xy=(.5,
                                                                            -1.4),
            fontsize=20) 
ax.annotate(r'$2, (\mathrm{i}\omega_n, \vec{k})$', xy=(.7, 1.3), fontsize=20) 

# 隐藏刻度
ax.set_xticks([])
ax.set_yticks([])

myfig.savefig('feynmanDiagram.jpg')    # 保存图片
