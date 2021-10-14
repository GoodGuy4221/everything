import random

test_array = [4, 5, 2, 6, 7, 3, 1, 8, 9, 0]


def quick_sort(array, first, last):
    print(array[first:last + 1])
    if first >= last:
        return

    pivot = array[random.randint(first, last)]
    i = first
    j = last
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

        quick_sort(array, first, j)
        quick_sort(array, i, last)


print(test_array)
quick_sort(test_array, 0, len(test_array) - 1)
print(test_array)
