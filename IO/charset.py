#
# coding=utf-8
#
#
print '指定编码，三种方式都可以'
print '# -*-coding:utf-8-*-'
print '# coding:utf-8'
print '# coding=utf-8'


# 迭代行
infile = open('utf8input.txt')
outfile = open('utf8output.txt', 'w')
for line in infile.readlines():
    outfile.write(line)



