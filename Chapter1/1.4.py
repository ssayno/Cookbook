import heapq

# 在某个集合中找到最大或者最小的 N 个元素
num = [1, 23, 993, 8493, 23, 23]
print(heapq.nlargest(3, num))
print(heapq.nsmallest(2, num))