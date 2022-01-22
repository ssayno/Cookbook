import re

# 估摸着在 (?(id/name)yes-pattern|no-pattern) 才会是 group 不需要在组别前面加上 \
patten = re.compile(r'(?P<name1><)?(?P<name>\w+@\w+(?:\.\w+)+)(?(name1)\?|$)')

print(patten.search('<418215971@qq.com?').group(0))
print(re.search(r'(.+) (?(1)thea|thea$)', 'the theaa'))
print(re.search(r'(.+) \1$', 'the theaa'))
print(re.search(r'(?P<quote>[\'\"]).*?(?P=quote)', '"this is a test"'))
print(re.escape('"https://www.python.org"'))