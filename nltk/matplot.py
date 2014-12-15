import numpy as np

import pylab as pl
# encoding=utf-8

# BeautifulSoup
import bs4
from bs4 import BeautifulSoup
import jieba
import jieba.posseg as pseg

import nltk
import numpy
import matplotlib
import matplotlib.pyplot as plt
import os

# path = '/home/zice/userProfile/word_div/get2/'
# fp = path+'1408213571.txt'
#
# infile = open(fp)
# tmp = ''
# for line in infile.readlines():
#     soup = BeautifulSoup(line)
#     tmp = tmp + soup.txt.get_text()
#
#
# words = pseg.cut(tmp)
# s = 'a'
# for w in words:
#     s = s + ' ' + w.flag[0:1]
#
# w = s.split(' ')
# fd = nltk.FreqDist(w)
#
# x= ['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'v', 'y',
# #      'x', 'z']
#
# # y = [fd.get(x[0]), fd.get(x[1]), fd.get(x[2]), fd.get(x[3]), fd.get(x[4]), fd.get(x[5]), fd.get(x[6]), fd.get(x[7]),
# #      fd.get(x[8]), fd.get(x[9]), fd.get(x[10]), fd.get(x[11]), fd.get(x[12]), fd.get(x[13]), fd.get(x[14]),
# #      fd.get(x[15]), fd.get(x[16]), fd.get(x[17]), fd.get(x[18]), fd.get(x[19]), fd.get(x[20]), fd.get(x[21]),
# #      fd.get(x[22]), fd.get(x[23]), fd.get(x[24])]
#
# x = ['a', 'c', 'b', 'e', 'd', 'g', 'f']
# y = [fd.get(x[0]), fd.get(x[1]), fd.get(x[2]), fd.get(x[3]), fd.get(x[4]), fd.get(x[5])]
# print fd.get(x[0]), ' ', fd.get(x[1]), ' ', fd.get(x[2]), ' ', fd.get(x[3]), ' ', fd.get(x[4]), ' ', fd.get(x[5])

# x = ['a', 'c', 'b', 'e', 'd']
x = [1, 2, 3, 4, 5]
y = [961, 463, 98, 919, 1570]


fig = pl.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 'ro')

ticks = ax.set_xticks([1, 2, 3, 4, 5])
labels = ax.set_xticklabels(['a', 'c', 'b', 'e', 'd'], rotation=30, fontsize='small')
ax.axis([0, 5, 0, 1000])
pl.show()
