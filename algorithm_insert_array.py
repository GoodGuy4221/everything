import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

number = 51
position = 2
# array.insert(position, number)
# print(array)

array.append(None)
print(array)
i = len(array) - 1
while position < i:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
    print(array)

array[position] = number
print(array)

array_new = array[:position] + [number] + array[position:]
print(array)
