#Random number generation
# Generating an array with random values inside an interval
# Getting unique items in an array
# Getting indices of unique elements
# Getting occurence of each element

import numpy

#1)Generating an array with random values inside an interval
max_value = 5
num_rows = 4
num_cols = 3
random_number_generator = numpy.random.default_rng()
random_array = random_number_generator.integers(max_value + 1, size=(num_rows, num_cols))
print('\n',random_array)
print('\n')

#2)Getting unique items in an array
max_value = 4
num_rows = 1
num_cols = 6
random_array2 = random_number_generator.integers(max_value + 1, size=(num_rows, num_cols))
print('Random array: ', random_array2)

#3)Getting indices of unique elements
unique_values, unique_values_indices = numpy.unique(random_array2, return_index=True)
print('Random array unique values: ', unique_values)
print('Unique values indices: ', unique_values_indices)

#4)Getting occurence of each element
unique_values, occurrence_count = numpy.unique(random_array2, return_counts=True)
print('Unique values occurence: ', occurrence_count)