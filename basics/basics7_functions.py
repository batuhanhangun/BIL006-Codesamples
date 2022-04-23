#Functions

def user_function():
    #Defining a function without parameter
    print("This is a user function named " +  user_function.__name__)
  
#Calling a function
user_function()

def capitalize_string(input_string: str):
    #Defining a function with parameters
    print("Input: " + input_string + "\nCapitalized input: " + input_string.upper())

#Passing argument to a function with one parameter
test_string = 'küçük'
capitalize_string(test_string)

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
