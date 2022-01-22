import re


text1 = '2021/1/16'
text2 = '2021 1 16'
text3 = f"{text1}, I can give you some help, {text2}"
print(text3)
patten = re.compile(r'(\d+)(?:/| )(\d+)(?:/| )(\d+)')
# 其中 \1 \2 \3 表示捕获组的数量
print(patten.sub(r'\1-\2-\3', text3))
# subn 返回替换的结果和次数
print(patten.subn(r'\1-\2-\3', text3))