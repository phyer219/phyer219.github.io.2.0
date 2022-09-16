import matplotlib.pyplot as plt

plt.plot([1], [1], marker=(5, 1, 0), markersize=30, mfc='none', mec='k', mew=1)

for i in range(4):
    plt.plot([1], [1], marker='o', markersize=30-5*i,
             mfc='none', mec='w', mew=1)

plt.plot([1], [1], marker=(5, 1, 0), markersize=30, mfc='gold', mec='k', mew=0)
plt.savefig('fig2.png')
