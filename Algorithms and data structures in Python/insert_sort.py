test_array = [4, 5, 2, 6, 7, 3, 1, 8, 9, 0]

# O(n**2)
for i in range(len(test_array)):
    spam = test_array[i]
    j = i
    while test_array[j - 1] > spam and j > 0:
        test_array[j] = test_array[j - 1]
        j -= 1
    test_array[j] = spam
    print(test_array)
