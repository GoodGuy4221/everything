test_array = [5, 8, 0, 6, 1, 3, 2, 4, 9, 7]

for i in range(1, len(test_array)):
    save = test_array[i]
    while i > 0 and test_array[i - 1] > save:
        test_array[i] = test_array[i - 1]
        i -= 1
    test_array[i] = save

print(test_array)
