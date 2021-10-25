def calc(*args):
    result = ''
    for i in range(len(args)):
        if i % 1:
            if args[i] not in ['+', '-', '*', '/']:
                raise NameError
        result += args[i]
    return eval(result)


if __name__ == '__main__':
    print(calc('51', '+', '21', '-', '3'))
