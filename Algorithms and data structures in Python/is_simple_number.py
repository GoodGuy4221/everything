def is_simple_number(n: (int, float)) -> bool:
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(is_simple_number(51))
    print(is_simple_number(52))
    print(is_simple_number(52))
