from collections import deque


# 队列的好处（保留有限的历史记录）
# 从队列两端添加和弹出元素复杂度都是 O(1)，用列表能实现对队列这个概念，但是复杂度到了 O(N)

# maxlen 创建指定长度的队列，当有新记录加入而队列已经满了的时候，自动移除最老的记录
q = deque(maxlen=3)
print(q)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(39)
print(q)
q.pop()
print(q)
q.popleft()
print(q)