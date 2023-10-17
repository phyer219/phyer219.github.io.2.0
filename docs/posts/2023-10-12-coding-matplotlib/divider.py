import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np


fig = plt.figure(figsize=[8, 4])
ax_1 = fig.add_subplot(1, 2, 1)
ax_2 = fig.add_subplot(1, 2, 2)

divider1 = make_axes_locatable(ax_1)
ax_cb1 = divider1.new_horizontal(size='5%', pad=.05)
fig.add_axes(ax_cb1)

divider2 = make_axes_locatable(ax_2)
ax_cb2 = divider2.new_horizontal(size='5%', pad=.05)
fig.add_axes(ax_cb2)

im1 = ax_1.imshow(np.random.randn(100, 100), origin='lower', cmap='rainbow')
im2 = ax_2.imshow(100*np.random.randn(100, 100), origin='lower', cmap='rainbow')
fig.colorbar(im1, ax_cb1)
fig.colorbar(im2, ax_cb2)
fig.savefig('divider.png', transparent=True)