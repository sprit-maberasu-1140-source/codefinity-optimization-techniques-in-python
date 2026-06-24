# Import the benchmarking decorator
import os
os.system('wget https://content-media-cdn.codefinity.com/courses/8d21890f-d960-4129-bc88-096e24211d53/section_1/chapter_3/decorators.py 2>/dev/null')
from decorators import timeit_decorator
import numpy as np
from copy import deepcopy

numbers = np.arange(100000)

# Define and decorate the first function
@timeit_decorator(number=100)
def square_array_slow(array):
    array = deepcopy(array)
    for i in range(len(array)):
        array[i] = array[i] **2
    return array

# Define and decorate the second function
@timeit_decorator(number=100)
def square_array_fast(array):
    array = deepcopy(array)
    return array ** 2

squares_array_1 = square_array_slow(numbers)
squares_array_2 = square_array_fast(numbers)
# Check if the arrays are equal
if np.array_equal(squares_array_1, squares_array_2):
    print('The arrays are equal')