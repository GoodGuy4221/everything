from random import randint


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Начните просматривать каждый элемент списка один за другим,
        # сравнивая его с соседним значением. С каждым
        # итерация, часть массива, на которую вы смотрите
        # сжимается, потому что остальные элементы уже были
        # отсортировано.
        for j in range(n - i - 1):
            # Создать флаг, который позволит функции
            # преждевременно завершить работу, если нечего сортировать
            already_sorted = True
            if array[j] > array[j + 1]:
                # Если объект, на который вы смотрите, больше, чем его
                # соседнее значение, затем поменяйте их местами
                array[j], array[j + 1] = array[j + 1], array[j]
                # Поскольку вам пришлось поменять местами два элемента,
                # устанавливаем флаг ʻalready_sorted` на `False`, чтобы
                # алгоритм не завершается преждевременно
                already_sorted = False
        # Если на последней итерации не было свопов,
        # массив уже отсортирован, и вы можете завершить
        if already_sorted:
            break
    return array


if __name__ == '__main__':
    LENGTH_ARRAY = 100
    test_array = [randint(0, 100) for _ in range(LENGTH_ARRAY)]
    print(f'no sorted\n{test_array}')
    bubble_sort(test_array)
    print(f'sorted\n{test_array}')
