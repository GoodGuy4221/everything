from best_bubble_sorted import bubble_sort
from sorting import run_sorting_algorithm
from random import randint

ARRAY_LENGTH = 1000
test_array = [randint(0, 100) for _ in range(ARRAY_LENGTH)]
print(f'no sorted\n{test_array}')
run_sorting_algorithm(algorithm="bubble_sort", array=test_array)
print(f'sorted\n{test_array}')
