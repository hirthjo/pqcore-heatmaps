import matplotlib.pyplot as plt
import numpy as np
import json
import collections
import sys
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.colors as colors
import matplotlib.ticker as ticker

data = []
with open(sys.argv[1], 'r') as file:
    data = json.loads(file.readline().replace('nil', '1').replace(' ', ','))

dict_data_size = collections.defaultdict(lambda: collections.defaultdict(int))
for tu in data:
    if tu[0]!=0 and tu[1] != 0 and tu[2] != 0:
        dict_data_size[tu[0]][tu[1]] = tu[2]
    elif tu[0]!= 0 and tu[1] != 0 and tu[2] == 0:
        dict_data_size[tu[0]][tu[1]] = 1



fig = plt.figure()
ax1 = fig.add_subplot()  # size


###########################################################
ax1.set(xlabel='p', ylabel='q')
_p_size = sorted(list(dict_data_size.keys()))
_k_size = sorted(
    list({key for p in _p_size for key in dict_data_size[p].keys()}))


p_size, k_size = np.mgrid[_p_size[0]:_p_size[-1]+1,_k_size[0]:_k_size[-1]+1]


top_size = np.array([[dict_data_size[_p_size[i]][_k_size[j]] for j in range(0, len(_k_size))]
                     for i in range(0, len(_p_size))])

pcm = ax1.pcolormesh(p_size, k_size, top_size,
                     # norm=colors.LogNorm(vmin=top_size.min(),
                     #                     vmax=top_size.max()),
                       cmap='Reds')
for item in ([ax1.title, ax1.xaxis.label, ax1.yaxis.label] +
             ax1.get_xticklabels() + ax1.get_yticklabels()):
    item.set_fontsize(36)

cbar = fig.colorbar(pcm, ax=ax1, extend='max')
#cbar = fig.colorbar(pcm, ax=ax3, extend='max',format=ticker.ScalarFormatter()) for logarithmic scale
#cbar.ax.set_major_formatter(matplotlib.ticker.ScalarFormatter())

cbar.ax.tick_params(labelsize=36) 
#### set axis ticks
ax1.set_xticks([i for i in range(1,6)])
ax1.set_yticks([2*i for i in range(1,5)])
cbar.set_ticks([i*4 for i in range(1,6)])

plt.show()
