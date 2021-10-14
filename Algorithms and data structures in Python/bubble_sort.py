test_array = [4, 5, 2, 6, 7, 3, 1, 8, 9, 0]

# O(n**2)
n = 0
for _ in test_array:
    n += 1
    for i in range(len(test_array) - n):
        if test_array[i] > test_array[i + 1]:
            test_array[i], test_array[i + 1] = test_array[i + 1], test_array[i]
    print(test_array)
