#Functions

#Defining a function without parameter
def user_function():
    print("This is a user function named " +  user_function.__name__)
  
#Calling a function
user_function()

#Defining a function with parameters
def capitalize_string(input_string: str):
    print("Input: " + input_string + "\nCapitalized input: " + input_string.upper())

#Passing argument to a function with one parameter
test_string = "küçük"
capitalize_string(test_string)

#Defining a function with more than one parameters
def print_user_info(input_name: str, input_surname: str, input_age: int):
    print("Name: " + input_name + "\nSurname: " + input_surname + "\nAge: " + str(input_age))
    
#Passing argument to a function with two parameters
name = "Thomas"
surname = "Shelby"
age = 25
print_user_info(name, surname, age)

#Syntax error. Argument order is important
#print_user_info(age, name, surname)

#Passing keyword arguments to a function with two parameters (argument order is NOT important)
print_user_info(input_age=41, input_surname="White", input_name="Walter")

#Defining a function with default parameters
def student_info(student_name: str, student_surname: str, student_id: int, is_enrolled = False):
    print("Name: " + student_name + "\nSurname: " + student_surname + "\nID: " + str(student_id) + "\nEnrolled: " + str(is_enrolled))

#Passing keyword arguments to a function with default arguments
name = "Mika"
surname = "Hakkinen"
student_id = 321412512
student_info(name, surname, student_id)