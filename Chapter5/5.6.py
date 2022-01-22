import io

# 本节的作用是将一段文字或者二进制字符写入类似文件的对象上
s = io.StringIO()
print(type(s))
print(s.write('hello, python\n'))
print(len('hello, python\n'))
print("can you help me", file=s)
print(s.getvalue())
# 二进制数据
ss = io.BytesIO()
ss.write(b'hello, write')
print(ss.getvalue())
