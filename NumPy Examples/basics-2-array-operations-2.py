#Array Operations -2
# Arithmetic operations
# Getting max, min and sum
# Getting inverse of a matrix
# Sorting an array
# Reversing an array

import numpy

#1)Arithmetic operations
#Summation
array1 = numpy.array([-1, 3, 9])
print('\n',array1)
print('\n')
array2 = numpy.array([2, -3, -5])
print(array2)
print('\n')
array3 = array1 + array2
print(array3)
array3 = numpy.add(array1, array2)
print(array3)
print('\n')

#Multiplication
array4 = array1 * array2
print(array4)
print('\n')
array4 = numpy.multiply(array1, array2)
print(array4)
print('\n')

#Division
array5 = array1 / array2
print(array5)
print('\n')
array5 = numpy.divide(array1, array2)
print(array5)
print('\n')

#Power
array6 = array1 ** 2
print(array6)
print('\n')
array6 = numpy.power(array1, 2)
print(array6)
print('\n')

#Square root
array7 = numpy.sqrt(array6)
print(array7)
print('\n')


array8 = numpy.array([30, 60])
array9 = numpy.cos(array8)
print(array9)
print('\n')
array10 = numpy.sin(array8)
print(array10)
print('\n')

#Matrix multiplication
array1 = numpy.array([[-1, 0], [0, -1]])
array2 = numpy.array([[3, 2], [6, 3]])
array3 = numpy.matmul(array1, array2)
print(array1)
print('\n')
print(array2)
print('\n')
print(array3)

#2)Max, min and sum
max_val = array3.max()
min_val = array3.min()
sum_val = array3.sum()
f_str = f"Max:{max_val} \tMin:{min_val} \tSum:{sum_val}"
print(f_str)
print('\n')

#3)Getting inverse of a matrix
resistor_matrix = numpy.array([[3, -1, 5], [1, -1, 0], [-4, 2, 2]])
print('R(ohm):', resistor_matrix)
print('\n')
electrical_potential_matrix = numpy.array([-20, 30, 0])
print('V(volt):', electrical_potential_matrix)
print('\n')
inverse_resistor_matrix = numpy.linalg.inv(resistor_matrix)
print('R^-1:', inverse_resistor_matrix)
print('\n')
#Finding currents by using inverse matrix and matrix multiplication
current_matrix = numpy.matmul(inverse_resistor_matrix, electrical_potential_matrix)
print('I(ampere):', current_matrix)
print('\n')

#4)Sorting an arrays
sorted_array = numpy.sort(current_matrix)
print('I(ampere)[SORTED]:', sorted_array)
print('\n')

#5)Reversing an array
reversed_array = numpy.flip(sorted_array)
print('I(ampere)[SORTED+REVERSED]:', reversed_array)
print('\n')