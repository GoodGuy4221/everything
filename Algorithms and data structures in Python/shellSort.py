test_array = [5, 8, 0, 6, 1, 3, 2, 4, 9, 7]


def shell_sort(list_number):
    def get_step(list_number):
        step = len(list_number) // 2
        steps = [step]
        while not step == 1:
            step = step // 2
            steps.append(step)

        return steps

    cur_steps = get_step(list_number)

    for s in cur_steps:
        for i in range(0, len(list_number)):
            j = list_number[i]
            current = i
            while j < list_number[current - s] and current > 0:
                list_number[current] = list_number[current - s]
                current -= s
            list_number[current] = j


shell_sort(test_array)
print(test_array)
