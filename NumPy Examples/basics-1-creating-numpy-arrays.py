import numpy

#1)Arrays with only row (row vector)
#Numeric array
first_numpy_array = numpy.array([-7, -5, -3, 0, 3, 5, 7])
print('\n')
print(first_numpy_array)
print('Type: ' + str(type(first_numpy_array)))
print('\n')
#String array
second_numpy_array = numpy.array(['orange', 'lemon'])
print('Type: ' + str(type(second_numpy_array)))
print(second_numpy_array)
#Combined array
third_numpy_array = numpy.array(['orange', 1])
print('Type: ' + str(type(third_numpy_array)))
print(third_numpy_array)
print('\n')


#2)Arrays with only column (column vector)
#Numeric array
first_numpy_array = numpy.array([[-7, -5, -3, 0, 3, 5, 7]]).T
print(first_numpy_array)
print('\n')
#String array
second_numpy_array = numpy.array([['orange', 'lemon']]).T
print(second_numpy_array)
print('\n')
#Combined array
third_numpy_array = numpy.array([['orange', 1]]).T
print(third_numpy_array)
print('\n')


#3)Arrays with rows and columns (matrix)
numpy_matrix = numpy.array([[6, 4, 2, 0], [-1, 0, 22, 49], [99, 110, 125, 131]])
print(numpy_matrix)
print('Type: ' + str(type(numpy_matrix)))
print('\n')

#4)Creating an empty matrix/vector
num_rows = 2
num_cols = 3
empty_vector = numpy.empty(2)
print(empty_vector) #initial values changes at each execution
print('\n')
empty_matrix = numpy.empty((num_rows, num_cols)) #initial values changes at each execution
print(empty_matrix) 
print('\n')


#5)Creating a zero matrix/vector
zero_vector = numpy.zeros(2)
print(zero_vector) 
print('\n')
zero_matrix = numpy.zeros((num_rows, num_cols))
print(zero_matrix) 
print('\n')

#6)Creating a matrix/vector filled with ones
ones_vector = numpy.ones(2)
print(ones_vector) 
print('\n')
ones_matrix = numpy.ones((num_rows, num_cols))
print(ones_matrix) 
print('\n')

#7)Creating an array with a range of elements
array_end = 6
arange_vector = numpy.arange(array_end + 1)
print(arange_vector) 
print('\n')

#8)Creating an array with a range of elements by using step size
array_begin = 25
array_end = 55
step_size = 5
arange_vector = numpy.arange(array_begin, array_end, step_size)
print(arange_vector) 
print('\n')

#9)Creating an array with values that are spaced linearly in the given interval
array_begin = 25
array_end = 35
total_numbers = 5
arange_vector = numpy.linspace(array_begin, array_end, num=total_numbers)
print(arange_vector) 
print('\n')



