from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    # Настройте контекст и подготовьте вызов указанного Алгоритма
    # с использованием предоставленного массива. Только импортировать
    # функция алгоритма, если это не встроенная функция sorted()
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    # Выполнить код десять раз и каждый раз
    # вернуть время в секундах
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    # Наконец, покажите название алгоритма и
    # минимальное время, необходимое для его выпонения
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    ARRAY_LENGTH = 10000
    # Сгенерировать массив элементов `ARRAY_LENGTH`, состоящий из
    # случайных целых значений от 0 до 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Вызвать функцию, используя имя алгоритма сортировки
    # и массив, который вы только что создали, передать ей
    run_sorting_algorithm(algorithm="sorted", array=array)
