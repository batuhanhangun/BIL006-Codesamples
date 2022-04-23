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
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.



print("=====================================================")
print("For loop")
for iterator_variable2 in range(5):
  print(iterator_variable2)
print('\n')

for iterator_variable2 in range(0, 8):
  print(iterator_variable2)
print('\n')
 
#Increment the sequence with 2 (default value = 1):
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
