from collections import deque

my_deque = deque([1, 2, 3, 4, 5])
print(f'{my_deque=}')
my_deque.append(51)
my_deque.appendleft(21)
print(f'{my_deque=}')
my_deque.count(0)
print(f'{my_deque=}')
my_deque.rotate(2)
print(f'{my_deque=}')
my_deque.rotate(-2)
print(f'{my_deque=}')

my_dequeE = deque([1, 2, 3, 4, 5], maxlen=5)
print(my_dequeE)
my_deque.appendleft(0)
print(my_dequeE)
