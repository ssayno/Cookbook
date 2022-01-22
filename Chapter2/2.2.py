import re


filename = 'spam.txt'
print(filename.endswith('.txt'))
url = 'https://www.google.com'
print(url.startswith('https:'))
# 当你需要对多个进行检查的时候，可以传入元组
print(url.startswith(('https:', 'http:', 'ftp:')))
# 或者使用正则?
try:
    print(url.startswith(re.compile('https?')))
except Exception as e:
    print(e.args)
# 换个方式就可以了
patten = re.compile('(?P<start>https?:|ftp:)')
print(re.match(patten, url).group('start'))