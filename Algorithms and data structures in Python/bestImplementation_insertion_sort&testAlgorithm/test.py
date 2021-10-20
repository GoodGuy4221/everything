from bestImplementation_insertion_sort import insertion_sort, insertion_sorted
from sorting import run_sorting_algorithm
from random import randint

ARRAY_LENGTH = 1000
test_array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

# Algorithm: insertion_sort. Minimum execution time: 0.30071849998785183
run_sorting_algorithm(algorithm="insertion_sort", array=test_array)
# Algorithm: insertion_sorted. Minimum execution time: 0.403795899997931
run_sorting_algorithm(algorithm="insertion_sorted", array=test_array)
