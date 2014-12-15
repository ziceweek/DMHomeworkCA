__author__ = 'zice'
import numpy
import matplotlib.pyplot as plt
from pylab import *
from numpy import *
from matplotlib import axes
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# # x = ['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'v', 'y', 'x']
# y = [0.0331, 0.0146, 0.0034, 0.0204, 0.0524, 0.0002, 0.0076, 0.004, 0.0, 0.001, 0.0016, 0.0357, 0.006, 0.0083, 0.171, 0.0068, 0.0171, 0.0024, 0.0546, 0.0615, 0.0094, 0.1748, 0.011, 0.303]
# plt.plot(x, y, 'ro')
# plt.xlabel(u'\u2103', fontproperties='SimHei')
# plt.axis([0, 25, 0, 1])

x = arange(-2, 2, 0.001)
y = 3*x*log(x)-1.0/36*exp(-(36.0*x-36.0/exp(1))**4)
plt.plot(x,y)


plt.show()