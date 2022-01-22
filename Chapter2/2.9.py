import re
import unicodedata


s1 = "Spicy Jalape\u00f1o"
s2 = "Spicy Jalapen\u0303o"
print(s1, id(s1))
print(s2, id(s2))
# 本小结的作用是将 unicode 字符转化统一
# NFC 表示的之字符全组成， NFD 表示的是字符分解组成，如下例子可见
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1, t2)
print(ascii(t1), ascii(t2))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3, t4)
print(ascii(t3), ascii(t4))