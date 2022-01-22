import re
line = 'asdf kedf;afjalkf[afaklj,aa    dd'
print(re.split(r'[;,\s]\s*', line))
# 捕获组匹配
print(re.split(r'(;|,|\s)\s*', line))
# 非捕获组匹配
print(re.split(r'(?:;|,|\s)\s*', line))
# 关于匹配组和非匹配组，可以查看官方文档，https://docs.python.org/zh-cn/3/howto/regex.html
