import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array.sort()
print(array)

find_ = int(input('What to look for? '))
position = len(array) // 2
left = 0
right = len(array) - 1

while find_ != array[position] and left <= right:
    if find_ > array[position]:
        left = position + 1
    elif find_ < array[position]:
        right = position - 1
    position = (left + right) // 2


print('element no' if left > right else f'element {find_} in cell {position}')
