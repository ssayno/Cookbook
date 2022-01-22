# 这节讲的就是数字的进制
# 有前缀
print(f"10 的八进制 {10:#o}")
print(f"10 的十六进制 {10:#X}")
print(f"10 的二进制 {10:#b}")
# 无前缀
print(f"10 的八进制 {10:o}")
print(f"10 的十六进制 {10:X}")
print(f"10 的二进制 {10:b}")
# format 格式
print("10 的八进制 {:o}".format(10))
print("10 的十六进制 {:X}".format(10))
print("10 的二进制 {:b}".format(10))
# 或者直接使用函数
print(bin(10))
print(oct(10))
print(hex(10))