def insertion_sort(array):
    # Цикл от второго элемента массива до
    # последний элемент
    for i in range(1, len(array)):
        # Это элемент, который мы хотим разместить в
        # правильное место
        value = array[i]
        # Инициализировать переменную, которая будет использоваться для
        # найти правильную позицию указанного элемента
        # `value`
        last_i = i - 1
        # Просмотрите список элементов (слева
        # часть массива) и найдите правильную позицию
        # элемента, на который ссылается `value`. Сделай это только
        # если value меньше соседних значений.
        while last_i >= 0 and array[last_i] > value:
            # Сдвинуть значение на одну позицию влево
            # и переместите last_i, чтобы указать на следующий элемент
            # (справа налево)
            array[last_i + 1] = array[last_i]
            last_i -= 1
        # Когда вы закончите сдвигать элементы, вы можете расположить
        # `value` в правильном месте
        array[last_i + 1] = value
    return array


# best
def insertion_sorted(array):
    for i in range(1, len(array)):
        paste_el = array[i]
        while i > 0 and array[i - 1] > paste_el:
            array[i] = array[i - 1]
            i -= 1
        array[i] = paste_el
