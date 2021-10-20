def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if array[min_index] > array[j]:
                min_index = j
        if not min_index == i:
            temp = array[i]
            array[i], array[min_index] = array[min_index], temp
