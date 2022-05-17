#Array Operations -1
# Accessing numpy array elements
# Concatenating two arrays
# Getting array shape
# Conditional indexing

import numpy

#1)Accessing numpy array elements
#Accesing an element in a 1d array 
numpy_array = numpy.array([-1, 5, 6, 8, -55, 66, 88, -54])
element_index = 6
selected_element = numpy_array[element_index]
f_str0 = f"numpy_matrix[{element_index}] = {selected_element}"
print('\n' + f_str0)
print('Type: ' + str(type(element_index)))
print('\n')

numpy_matrix = numpy.array([[6, 4, 2, 0], [-1, 0, 22, 49], [99, 110, 125, 131]])
print(numpy_matrix)
print('Type: ' + str(type(numpy_matrix)))
print('\n')

selected_row = 0
selected_col = 1
#Accesing a row by using (row, :) notation
row_elements = numpy_matrix[selected_row, :]
f_str1 = f"numpy_matrix[Row = {selected_row}] = {row_elements}"
print(f_str1)
print('Type: ' + str(type(row_elements)))
print('\n')
#Accesing column  by using (:, col) notation
col_elements = numpy_matrix[:, selected_col]
f_str2 = f"numpy_matrix[Col = {selected_col}] = {col_elements}"
print(f_str2)
print('Type: ' + str(type(col_elements)))
print('\n')
#Accessing a single element by using (row, col) notation
single_element = numpy_matrix[selected_row, selected_col]
f_str3 = f"numpy_matrix[{selected_row}, {selected_col}] = {single_element}"
print(f_str3)
print('Type: ' + str(type(single_element)))
print('\n')

#2)Concatenating two arrays
array1 = numpy.array([-3, 0, 9, -23])
print(array1)
print('\n')
array2 = numpy.array([48, -6, 32, -76])
print(array2)
print('\n')
#By using concatenate function
concat_array = numpy.concatenate((array1, array2))
print(concat_array)
print('Type: ' + str(type(concat_array)))
print('\n')
#By using [array1, array2] notation
concat_array2 = numpy.array([array1, array2])
print(concat_array2)
print('Type: ' + str(type(concat_array)))
print('\n')

#3)Getting array shape
total_rows, total_cols = numpy_matrix.shape
f_str = f"numpy_matrix: {total_rows}x{total_cols}x1"
print(numpy_matrix)
print(f_str)
print('Type: ' + str(type(numpy_matrix)))
print('\n')

#4) Conditional indexing
test_array = numpy.array([[0 , -2, 23, 34, 83], [1, -5, 98, -44, 13]])
print(test_array[test_array < 0])

greater_than_twenty = (test_array >= 20)
print(test_array[greater_than_twenty])

test_array2 = test_array[(test_array > 20) & (test_array < 90)]
print(test_array2)

