import re
from fnmatch import fnmatch, fnmatchcase


# 这里就是使用 shell 的通配符语法了，当然，对我，我比较喜欢 shell 语法，当然会学一手
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '*.TXT'))
# 注意大小写
print(fnmatchcase('foo.txt', '*.TXT'))