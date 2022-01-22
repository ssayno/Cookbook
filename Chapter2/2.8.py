import re


# 值得注意的是 python 正则表达式中的 . 匹配除了换行符之外的任意字符，但是你可以手动让他匹配
text1 = "/* this is a comment */"
text2 = '''/* This is multiline comment
              can you know */
'''
patten = re.compile(r'/\*(.*?)\*/', flags=re.S)
# ?: 为非捕获组，所以你得再加一个括号
patten2 = re.compile(r'/\*((?:.|\n)*)\*/')
print(patten.findall(text1))
print(patten.findall(text2))
print(patten2.findall(text2))
