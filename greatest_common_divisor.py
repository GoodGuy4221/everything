def greatest_common_divisor_cycle(n_1, n_2):
    while n_1 != n_2:
        if n_1 > n_2:
            n_1 -= n_2
        else:
            n_2 -= n_1
    return n_1


def greatest_common_divisor_recursion(n_1, n_2):
    if n_2 == 0:
        return n_1
    return greatest_common_divisor_recursion(n_2, n_1 % n_2)


print(greatest_common_divisor_cycle(51, 21))
print(greatest_common_divisor_recursion(51, 21))
