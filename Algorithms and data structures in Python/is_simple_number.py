def is_simple_number(n: int) -> bool:
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True


def eratosthenes(number: int):
    n = list(range(number + 1))
    n[0] = n[1] = False
    for i in range(2, number):
        if n[i]:
            for j in range(2 * i, number + 1, i):
                n[j] = False
    return [i for i in n if i]


if __name__ == '__main__':
    print(is_simple_number(51))
    print(is_simple_number(52))
    print(is_simple_number(2))
    print(eratosthenes(2))
    print(eratosthenes(50))
