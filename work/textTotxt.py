__author__ = 'zice'

#
# coding=utf-8
#
#
import re
import os
inpath = '/home/zice/userProfile/word_div/get/'
outpath = '/home/zice/userProfile/word_div/get2/'
fileList = os.listdir(inpath)

for filename in fileList:
    print(filename)
    infile = open(inpath + filename)
    outfile = open(outpath + filename, 'w')
    str1 = infile.read()
    infile.close()

    k = re.sub('text', 'txt', str1)
    print len(k)

    outfile.write(k)
    outfile.close()
