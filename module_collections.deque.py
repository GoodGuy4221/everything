from collections import deque

a = deque()
b = deque('hdsdgfhsdfgh')
print(a)
print(b)

b.append(7)
print(b)
b.appendleft(8)
print(b)
b.extend([51, 21, 94])
print(b)

b.extendleft([94, 52, 21])
print(b)

n = b.pop()
print(b, n)

l = b.popleft()
print(l, b)

b.insert(2, 555)
print(b)
