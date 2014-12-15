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


def read_and_get_text_in_tag(file_path='/home/zice/userProfile/word_div/get2/1043714862.txt'):
    infile = open(file_path)
    soup = BeautifulSoup(infile.read())
    weiboList = soup.find_all(name='txt')
    tmp = ''
    for w in weiboList:
        tmp += w.get_text()
    print tmp

    # tmp = ''
    # for line in infile.readlines():
    #    soup = BeautifulSoup(line)
    #    tmp = tmp + soup.txt.get_text()
    # print tmp

    return tmp


# return a fdist like {[a:23],[c:30],....} 'a' refer to adjective,'c' refer to conjunction
def cut_words_and_count_speech(document):

    words = pseg.cut(document)
    s = 'a'
    for w in words:
        s = s + ' ' + w.flag[0:1]
    w = s.split(' ')
    fdist = nltk.FreqDist(w)
    return fdist


def vector(fd):
    x = ['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'v',
         'y', 'x', 'z']

    # 計算詞的總數
    s = 0
    for index1 in range(0, 25):
        if fd.__contains__(x[index1]):
            s = s + fd.get(x[index1])

    # generate list
    y = []
    for index2 in range(0, 25):
        if fd.get(x[index2]):
            y.append(round(fd.get(x[index2])/float(s), 4))
        else:
            y.append(0.0)

    return y

doc = read_and_get_text_in_tag()
frdist = cut_words_and_count_speech(doc)
speech_list = vector(frdist)

outfile = open(outpath + filename, 'w')
# inpath = '/home/zice/userProfile/word_div/get/'
# outpath = '/home/zice/userProfile/word_div/get2/'
# fileList = os.listdir(inpath)
#
# for filename in fileList:
#     print(filename)
#     infile = open(inpath + filename)
#     outfile = open(outpath + filename, 'w')
#     str1 = infile.read()
#     infile.close()
#
#     k = re.sub('text', 'txt', str1)
#     print len(k)
#
#     outfile.write(k)
#     outfile.close()