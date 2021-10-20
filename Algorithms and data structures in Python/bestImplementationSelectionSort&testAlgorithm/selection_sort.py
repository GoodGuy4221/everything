def selection_sort(array):
    length_array = len(array)
    for i in range(length_array - 1):
        min_index = i
        for j in range(i + 1, length_array):
            if array[min_index] > array[j]:
                min_index = j
        if not min_index == i:
            array[i], array[min_index] = array[min_index], array[i]
