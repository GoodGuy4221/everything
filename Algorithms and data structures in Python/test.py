test_array = [5, 8, 0, 6, 1, 3, 2, 4, 9, 7]


def my_bubble_sort(list_):
    array_ = list_.copy()
    for i in range(len(array_)):
        for k in range(len(array_) - i - 1):
            if array_[k] > array_[k + 1]:
                array_[k], array_[k + 1] = array_[k + 1], array_[k]

    return array_


print(my_bubble_sort(test_array))
print(test_array)
