import random

test_array = [4, 5, 2, 6, 7, 3, 1, 8, 9, 0]

n = 1
while n < len(test_array):
    for i in range(len(test_array) - 1):
        if test_array[i] > test_array[i + 1]:
            test_array[i], test_array[i + 1] = test_array[i + 1], test_array[i]
    n += 1
    print(test_array)
