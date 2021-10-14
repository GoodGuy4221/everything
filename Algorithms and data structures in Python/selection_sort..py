test_array = [4, 5, 2, 6, 7, 3, 1, 8, 9, 0]

# O(n**2)
for i in range(len(test_array) - 1):
    current_min_el = i
    for j in range(i + 1, len(test_array)):
        if test_array[j] < test_array[current_min_el]:
            current_min_el = j
    test_array[current_min_el], test_array[i] = test_array[i], test_array[current_min_el]
    print(test_array)
