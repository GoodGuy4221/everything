import time


# def cash(func):
#     def wrapper(number, cash_data={1: 1, 2: 1}):
#         current_el = cash_data.get(number)
#         if not current_el:
#             current_el = func(number)
#             cash_data.update({number: current_el})
#         return current_el
#
#     return wrapper


def cash(func):
    def wrapper(number, cash_data=[1, 1]):
        if len(cash_data) <= number:
            current_el = func(number)
            cash_data.append(current_el)
        else:
            current_el = cash_data[number]
        return current_el

    return wrapper


@cash
def get_fibonacci_numbers(number):
    # quadratic complexity
    if number in [1, 2]:
        return 1
    else:
        return get_fibonacci_numbers(number - 1) + get_fibonacci_numbers(number - 2)


start_time = time.time()
print(get_fibonacci_numbers(480))
end_time = time.time()
print(f'time result {end_time - start_time}')
