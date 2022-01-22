import re


# 此处讲的主要是贪婪和非贪婪匹配
patten = re.compile(r'\"(.*)\"')
text = 'Computer says "no."'
print(patten.findall(text))
text2 = 'Computer says "no.", Phone says "yes."'
print(patten.findall(text2))
# 展示非贪婪匹配
print(re.findall(r'\"(.*?)\"', text))
print(re.findall(r'\"(.*?)\"', text2))
