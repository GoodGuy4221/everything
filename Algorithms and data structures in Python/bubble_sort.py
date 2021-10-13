test_array = [4, 5, 2, 6, 7, 3, 1, 8, 9, 0]

# O(n**2)
for _ in test_array:
    for i in range(len(test_array) - 1):
        if test_array[i] > test_array[i + 1]:
            test_array[i], test_array[i + 1] = test_array[i + 1], test_array[i]
    print(test_array)
