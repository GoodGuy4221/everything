from selection_sort import selection_sort
from timeit import timeit
from random import randint

LENGTH_ARRAY = 100
RANGE_FROM = 0
RANGE_UP_TO = 100
test_array = [randint(RANGE_FROM, RANGE_UP_TO) for _ in range(LENGTH_ARRAY)]

average_execution_time = timeit('selection_sort', globals=globals(), setup='test_array')
print(average_execution_time)
# selection_sort(test_array)
# print(test_array)
