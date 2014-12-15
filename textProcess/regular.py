__author__ = 'zice'
# encoding=utf-8
import re
pat = re.compile(r'\[.*\]')
string = '@你好[热情]'
result = pat.search(string)
s = result.start(0)
e = result.end(0)
print string[s:e]
k = re.findall('@', string)
print len(k)

