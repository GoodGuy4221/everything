import random

test_array = [5, 8, 0, 6, 1, 3, 2, 4, 9, 7]


def quick_sort(list_number, start=0, end=False):
    def part_sort(list_number, start, end, core_el):
        core = list_number[core_el]
        list_number[core_el], list_number[start] = list_number[start], list_number[core_el]

        # current
        a = start + 1
        # move
        b = start + 1
        while a <= end:
            if list_number[a] <= core:
                list_number[a], list_number[b] = list_number[b], list_number[a]
                b += 1
            a += 1

        list_number[start], list_number[b - 1] = list_number[b - 1], list_number[start]
        return b - 1

    if not end:
        end = len(list_number) - 1
    if end - start < 1:
        return

    core_el = random.randint(start, end)
    ind = part_sort(list_number, start, end, core_el)
    quick_sort(list_number, start, ind - 1)
    quick_sort(list_number, ind + 1, end)


quick_sort(test_array)
print(test_array)
