__author__ = 'zice'
# encoding=utf-8

# BeautifulSoup
import bs4
from bs4 import BeautifulSoup
# 结巴分词
import jieba
import jieba.posseg as pseg

import nltk
import numpy
import matplotlib
import matplotlib.pyplot as plt
import os


def todo(filepath):
    # path = '/home/zice/userProfile/word_div/get2/'
    # filepath = path+'1043714862.txt'
    # filepath = path+'1143641361.txt'
    # path = '/home/zice/userProfile/word_div/'
    # filepath = path+'1251872852.txt'

    infile = open(filepath)
    # newlist = []
    tmp = ''
    for line in infile.readlines():
        soup = BeautifulSoup(line)
    #    print soup.uid.get_text()
    #    newlist.append(soup.txt.get_text())
        tmp = tmp + soup.txt.get_text()

    print tmp

# 用词典统计
# d = dict()
# words = pseg.cut(tmp)
# for w in words:
#     if w.flag in d:
#         d[w.flag] += 1
#     else:
#         d[w.flag] = 1
# #    s = s + w.word + w.flag + ' '
# print d

    words = pseg.cut(tmp)
    s = 'a'
    for w in words:
        s = s + ' ' + w.flag[0:1]
    # print s

    w = s.split(' ')
    fdist = nltk.FreqDist(w)
    return fdist


inpath = '/home/zice/userProfile/word_div/get2/'
fileList = os.listdir(inpath)

i = 0

fig1 = plt.figure(1)
# fig2 = plt.figure(2)
ax1 = fig1.add_subplot(1, 1, 1)
# ax2 = fig2.add_subplot(1, 1, 1)

for filename in fileList[1:100]:
    fd = todo(inpath + filename)
    x = ['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'v',
         'y', 'x', 'z']
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    s = 0
    for index1 in range(0, 25):
        if fd.__contains__(x[index1]):
            s = s + fd.get(x[index1])
    y = []

    for index2 in range(0, 25):
        if fd.get(x[index2]):
            y.append(round(fd.get(x[index2])/float(s), 4))
        else:
            y.append(0.0)
    # y = [fd.get(x[0]), fd.get(x[1]), fd.get(x[2]), fd.get(x[3]), fd.get(x[4]), fd.get(x[5]), fd.get(x[6]),
    # fd.get(x[7]),
    #      fd.get(x[8]), fd.get(x[9]), fd.get(x[10]), fd.get(x[11]), fd.get(x[12]), fd.get(x[13]), fd.get(x[14]),
    #      fd.get(x[15]), fd.get(x[16]), fd.get(x[17]), fd.get(x[18]), fd.get(x[19]), fd.get(x[20]), fd.get(x[21]),
    #      fd.get(x[22]), fd.get(x[23]), fd.get(x[24])]

    print s
    # print y, '\n', x1
    # plt.plot(x1, y, 'ro')
    #
    # plt.title('Plot of words')
    # plt.axis([0, 25, 0, 1])
    # plt.xlabel('x axis')
    # plt.ylabel('y axis')

    color = ['r', 'g', 'b', 'y', 'm', 'k']
    y.sort()
    # ax.plot(x1, y, color[divmod(i, len(color))[1]]+'o')
    ax1.plot(x1, y, color[divmod(i, len(color))[1]])

    ticks1 = ax1.set_xticks(x1)
    labels1 = ax1.set_xticklabels(x, rotation=30, fontsize='small')
    ax1.axis([0, 25, 0, 0.02])

    # ax2.plot(x1, y, color[divmod(i, len(color))[1]])

    # ticks2 = ax2.set_xticks(x1)
    # labels2 = ax2.set_xticklabels(x, rotation=30, fontsize='small')
    # ax2.axis([0, 25, 0, 0.4])

    i += 1
plt.show()





