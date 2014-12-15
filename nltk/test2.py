__author__ = 'zice'
# encoding=utf-8
import matplotlib.pyplot as plt
import numpy

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([1, 200, 330, 154, 995])
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')

ax.set_xlabel('Stages')
plt.show()
