#Conditional statements
#If, If-Else, If-Elseif-Else
print("=====================================================")
print("Conditional Statements")

n1 = 145
n2 = 41
if n1 > n2:
  print("n1 is greater than n2")
  
n1 = 145
n2 = 41
if n2 > n1:
  print("n2 is greater than n1")
else:
  print("n1 is greater than n2")

n1 = 41
n2 = 41
if n2 > n1:
  print("n2 is greater than n1")
elif n1 > n2:
  print("n1 is greater than n2")
else:
  print("n1 is equal to n2")
print("=====================================================\n")


#Loops
#While loop
print("=====================================================")
print("While loop")
iterator_variable1 = 1
while iterator_variable1 < 6:
  print(iterator_variable1)
  iterator_variable1 += iterator_variable1
print('\n')

iterator_variable1 = 1
while iterator_variable1 < 6:
  print(iterator_variable1)
  if iterator_variable1 == 3:
    break
  iterator_variable1 += 1
print('\n')
  
iterator_variable1 = 0
while iterator_variable1 < 6:
  iterator_variable1 += 1
  if iterator_variable1 == 3:
    continue
  print(iterator_variable1)
print('\n')
  
print("=====================================================\n")

#For loop
# The a_sequence = range(n) function returns a consecutive sequence that consists of "n" numbers that start from 0 by default.



print("=====================================================")
print("For loop")
for iterator_variable2 in range(5):
  print(iterator_variable2)
print('\n')

#Defining a custom range between 0 and 8 (8 is not included in the sequence!)
for iterator_variable2 in range(0, 8):
  print(iterator_variable2)
print('\n')
 
#Increment the elements of a sequence with 2 (default value = 1)
for iterator_variable2 in range(1, 16, 2):
  print(iterator_variable2)
print('\n')

#Iterating a string
password = '123!*a421gfd'
for item in password:
  print(item)

#Iterating a list
shopping_list = ['eggs', 'milk', 'chocolate', 'water']
for item in shopping_list:
  print(item)
print("=====================================================\n")
