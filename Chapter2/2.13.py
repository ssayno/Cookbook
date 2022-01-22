import re


text = 'hello, world!'
print(text.ljust(20, '-'))
print(text.rjust(20, '='))
print(text.center(20, '+'))
# 对于 format ，使用 < > ^ 来进行对齐 指向左边就是做， 上就是居中对齐
print(format(text, '=<20'))
print(format(text, '->20'))
print(format(text, '-^20'))
# 对于格式化字符串一样可以操作
print(f'{text:=<20}')
print(f'{text:->20}')
print(f'{text:!^20}')
# 主要的是他们不仅仅可以对字符串进行操作，不推荐使用 % 进行格式化字符串
# 一般的格式为 [<^>]?width[,]?(.digits)? 其中 ? 表示可选，[,] 表示是否采用千分制
numbers = 13323423.423
print(numbers)
print(f'{numbers:=>20,.3f}')
print(f'{numbers:=>20,.3e}')


