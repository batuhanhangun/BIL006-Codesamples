#Numeric objects
number1 = 20
number2 = 30.5

print("==============================================================================")
print("Basic output")
#Basic output
print(number1)
print(number2)
print("==============================================================================")

print("==============================================================================")
print("Combining numeric type objects with string type objects")

#Combining numeric type objects with string type objects
# str(var) -> converts any suitable object into a string 
# type object and stores it in a temporary object
# without modifying the original input argument object
print("number1 = " + str(number1))
print("number2 = " + str(number2))


number3 = number1 + number2
print("number1 + number2 = " + str(number1+number2))
print("number3 = " + str(number3))

number4 = number3
print("number4 =" + str(number4))
print("==============================================================================")

print("==============================================================================")
print("Swapping values between two objects")
#Swapping values between two objects
# Swap -> object1, object2 = object2, object1
# No need to create a famous "temp" variable anymore!
print("\nValues of number1 and number2 before swap")
print("number1 = " + str(number1))
print("number2 = " + str(number2))
number1, number2 = number2, number1
print("\nValues of number1 and number2 after swap")
print("number1 = " + str(number1))
print("number2 = " + str(number2))
print("==============================================================================")
