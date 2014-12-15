__author__ = 'zice'

# encoding = utf-8
import os
import bs4
from bs4 import BeautifulSoup

path = '/home/zice/userProfile/word_div/get/'
# filepath = path+'1043714862.txt'
fileList = os.listdir(path)

for filename in fileList:
    print(filename)

#
# infile = open(filepath)
# for line in infile.readlines():
#     soup = BeautifulSoup(line)
#     print soup.uid
#     print soup.text
