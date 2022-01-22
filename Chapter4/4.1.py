from collections.abc import Iterable
from collections.abc import Iterator

print(f"List is 'Iterable': {isinstance([], Iterable)}")
print(f"Tuple is 'Iterable': {isinstance((), Iterable)}")
print(f"Dict is 'Iterable': {isinstance({}, Iterable)}")
print(f"String is 'Iterable': {isinstance('', Iterable)}")
print(f"Set is 'Iterable': {isinstance(set(), Iterable)}")

print("=" * 25)

print(f"List is 'Iterator': {isinstance([], Iterator)}")
print(f"Tuple is 'Iterator': {isinstance((), Iterator)}")
print(f"Dict is 'Iterator': {isinstance({}, Iterator)}")
print(f"String is 'Iterator': {isinstance('', Iterator)}")
print(f"Set is 'Iterator': {isinstance(set(), Iterator)}")
# 输出如下：
# List is 'Iterable': True
# Tuple is 'Iterable': True
# Dict is 'Iterable': True
# String is 'Iterable': True
# =========================
# List is 'Iterator': False
# Tuple is 'Iterator': False
# Dict is 'Iterator': False
# String is 'Iterator': False
# 迭代器一定是可迭代的，但是可迭代的不一定是迭代器（没有 __next__() 方法
items = [1, 2, 3]
print(type(items))
it = iter(items)
print(type(it))
