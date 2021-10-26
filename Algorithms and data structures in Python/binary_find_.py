def binary_find(indexed: (list, tuple), value) -> int:
    length = len(indexed)
    average, left, right = length // 2, 0, length - 1,

    while not value == indexed[average] and left <= right:
        if value > indexed[average]:
            left = average + 1
        elif value < indexed[average]:
            right = average - 1
        average = (left + right) // 2

    return -1 if left > right else average


if __name__ == '__main__':
    import random

    SIZE = 10
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    array.sort()
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(array)

    value_find = 5
    print(binary_find(array, value_find))
