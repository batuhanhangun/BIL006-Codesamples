#Functions

def user_function():
    #Defining a function without parameter
    print("This is a user function named " +  user_function.__name__)
  
#Calling a function
user_function()

print("====================================================================================================\n")

def capitalize_string(input_string: str):
    #Defining a function with parameters
    print("Input: " + input_string + "\nCapitalized input: " + input_string.upper())

#Passing argument to a function with one parameter
test_string = 'küçük'
capitalize_string(test_string)

print("====================================================================================================\n")

def print_user_info(input_name: str, input_surname: str, input_age: int):
    #Defining a function with more than one parameters
    print("Name: " + input_name + "\nSurname: " + input_surname + "\nAge: " + str(input_age))
    
#Passing argument to a function with two parameters
name = 'Thomas'
surname = 'Shelby'
age = 25
print_user_info(name, surname, age)

#print_user_info(age, name, surname)
#Syntax error. Argument order is important!

#Passing keyword arguments to a function with parameters (argument order is NOT important)
print_user_info(input_age = 41, input_surname = 'White', input_name = 'Walter')

print("====================================================================================================\n")

def student_info(student_name: str, student_surname: str, student_id: int, is_enrolled = False, scholarship = int(0)):
    #Defining a function with parameters which some of them have default arguments
    print("Name: " + student_name + "\nSurname: " + student_surname + "\nID: " + str(student_id) + "\nEnrolled: " + str(is_enrolled) + "\nScholarship: " + str(scholarship))

#Passing keyword arguments to a function with default arguments
name = 'Mika'
surname = 'Hakkinen'
student_id = 321412512
student_info(name, surname, student_id)
student_info(name, surname, student_id, is_enrolled = True)
student_info(name, surname, student_id, is_enrolled = True, scholarship = 40)

print("====================================================================================================\n")

def calculate_distance(point1_x: float, point1_y: float, point2_x: float, point2_y: float, norm = 'L2'):
    # A function definition with conditional statements and logical expressions
    if(not (norm == 'L1' or norm =='L2')):
        print("ERROR: Norm must be \'L1\' or \'L2\'")
        return #Use an empty 'return' to simply terminate the function
    elif(norm == 'L1'):
        return abs(point1_x - point2_x) + abs(point1_y - point2_y) #Use 'return' with some values to get results from a function
    else:
        return (((point1_x - point2_x)**2) + ((point1_y - point2_y)**2))**0.5

point1_x = 3
point2_x = 5
point1_y = 1 
point2_y = 2
distance_val = calculate_distance(point1_x, point1_y, point2_x, point2_y)
print("L2 norm: " + str(distance_val))
norm_type = 'L1'
distance_val = calculate_distance(point1_x, point1_y, point2_x, point2_y, norm_type)
print("L1 norm: " + str(distance_val))
norm_type = 'Minkowski'
distance_val = calculate_distance(point1_x, point1_y, point2_x, point2_y, norm_type)

print("====================================================================================================\n")

def add_vectors(array1, array2):
     # A function definition with conditional statements, logical expressions and for loop
    if(len(array1) != len(array2)):
        print("ERROR: Dimensionality mismatch. Len1 = " + str(len(array1)) + " Len2 = " + str(len(array2))),
        return
    else:
        array3 = [None] * len(array1)    
           
    for vector_iter in range(0, len(array3)):
        array3[vector_iter] = array1[vector_iter] + array2[vector_iter]
            
    return array3

array1 = [3, 5, 7]
array2 = [-1, -2, -3]
array3 = add_vectors(array1, array2)
print("Array1 = " + str(array1))
print("Array2 = " + str(array2))
print("Array3 = Array1 + Array2 =  " + str(array3))
array4 = [2, 5]
array5 = add_vectors(array1, array4)

