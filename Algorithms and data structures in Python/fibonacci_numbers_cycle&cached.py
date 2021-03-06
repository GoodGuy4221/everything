import time


def cached(func):
    def wrapper(number, cache_data=[1, 1]):
        if len(cache_data) <= number:
            current_el = func(number)
            cache_data.append(current_el)
        else:
            current_el = cache_data[number]
        return current_el

    return wrapper


@cached
def get_fibonacci_numbers_cycle(number: int) -> int:
    if number in [1, 2]:
        return 1
    last_1, last_2 = 1, 1
    for i in range(number - 1):
        current_el = last_1 + last_2
        last_1 = last_2
        last_2 = current_el

    return last_2


start_time = time.time()
print(get_fibonacci_numbers_cycle(5100))
end_time = time.time()
print(f'time result {end_time - start_time}')
