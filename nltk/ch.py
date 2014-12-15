__author__ = 'zice'
# encoding=utf-8
import nltk
import codecs
import numpy
import scipy
import matplotlib
from pprint import pprint

# text = ['中文', '英文', 'chaos'],
text = '13131 13131 afa aa tk 13131 tk  tk tk  hh hh hh hh'
# text = unicode(text, 'utf-8')
tl = text.split(' ')
# print len(text2)
fdist = nltk.FreqDist(tl)
token = fdist.keys()
print fdist.items()
print 'fdist:', fdist.items()

for item in token:
    print item

# rint fdist.items()[0][0]
# fdist.plot()
# CODEC = 'utf-8'
# print text2, 'dfadff'
# outfile = open('nltkOutput.txt', 'w')
# for item in fdist.items():
#    u = unicode(item.__str__(), 'ASCII')
#    print u
#    outfile.write(u.encode('utf-8')+'\n')
#print unicode(tl[1], 'utf-8')
# fdist.plot()

#
# FILE = 'unicode.txt'
# hello_out = u"Hell你好周杰伦\n"
# bytes_out = hello_out.encode(CODEC)
#
# print '1', bytes_out
# f = open(FILE, 'w')
# f.write(bytes_out)
# f.close()
#
# f = open(FILE, 'r')
# bytes_in = f.read()
# f.close()
# hello_in = bytes_in.decode(CODEC)
# print '2', hello_in