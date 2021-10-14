import random

test_array = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
random.shuffle(test_array)
print(test_array)


def shell_sort(array):
    assert len(array) < 4_000, 'Массив слишком большой для эффективной сортировки этим методом :P'

    def new_inc(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while inc:
            yield inc.pop()

    for cur_inc in new_inc(array):
        for i in range(cur_inc, len(array)):
            for j in range(i, cur_inc - 1, -cur_inc):
                if array[j - cur_inc] <= array[j]:
                    break
                array[j], array[j - cur_inc] = array[j - cur_inc], array[j]
            print(array)


shell_sort(test_array)
