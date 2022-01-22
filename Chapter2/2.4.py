import re


text1 = '2021/1/16'
text2 = '2021 1 16'
# 非捕获组模式
patten = re.compile(r'(\d+)(?:/| )(\d+)(?:/| )(\d+)')
print(re.match(patten, text1).group(0))
print(re.match(patten, text2))
text3 = f"{text1}, I can give you some help, {text2}"
print(re.match(patten, text3))
print(re.findall(patten, text3))
# 使用迭代也是可以的
for item in re.finditer(patten, text3):
    # 返回直接的组
    print(item.groups())