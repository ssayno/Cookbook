import re


# 字符串功能 strip 只能去除两边的字符，无法处理中间的，使用替换功能来解决这个功能
s = 'hello    world   a\n'
print(s)
print('--')
print(re.sub(r'\s+', ' ', s))