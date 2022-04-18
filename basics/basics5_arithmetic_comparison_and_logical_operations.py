#Arithmetic Operations on numeric objects
print("==============================================================================")
print("Arithmetic operations")
#Addition
# + operator: numeric3 = numeric1 + numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' - '+str(number2) + ' = ' + str(number1+number2))

#Summation
# - operator: numeric3 = numeric1 - numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' - '+str(number2) + ' = ' + str(number1-number2))

#Multiplication
# * operator: numeric3 = numeric1 * numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' * '+str(number2) + ' = ' + str(number1*number2))

#Division
# / operator: numeric3 = numeric1 / numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' / '+str(number2) + ' = ' + str(number1/number2))

#Power
# ** operator: result = base**power
number1 = 2
number2 = 3
print(str(number1)+' ^ '+str(number2) + ' = ' + str(number1**number2))
print(str(number1)+' ^- '+str(number2) + ' = ' + str(number1**-number2))

#Modulo
# % operator: remainder = numeric1 / numeric2
number1 = 4
number2 = 3
print(str(number1)+' % '+str(number2) + ' = ' + str(number1%number2))
print("==============================================================================")



#Comparison Operations on numeric objects
print("==============================================================================")
print("Comparison operations")
#Is equal?
# == operator: numeric3 = numeric1 == numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' == '+str(number2) + ' = ' + str(number1==number2))

#Is not equal?
# != operator: numeric3 = numeric1 != numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' != '+str(number2) + ' = ' + str(number1!=number2))

#Is greater than?
# > operator: numeric3 = numeric1 > numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' > '+str(number2) + ' = ' + str(number1>number2))

#Is smaller than?
# < operator: numeric3 = numeric1 < numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' < '+str(number2) + ' = ' + str(number1<number2))

#Is smaller or equal than?
# <= operator: numeric3 = numeric1 <= numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' <= '+str(number2) + ' = ' + str(number1<=number2))

#Is greater than?
# => operator: numeric3 = numeric1 => numeric2
number1 = 20.235
number2 = 25
print(str(number1)+' >= '+str(number2) + ' = ' + str(number1>=number2))
print("==============================================================================")


#Logical Operations
print("==============================================================================")
print("Logical Operations")
#and
# and operator: numeric3 = numeric1 and numeric2
bool1 = True
bool2 = True
print(str(bool1)+' and '+str(bool2) + ' = ' + str(bool1 and bool2))
bool1 = True
bool2 = False
print(str(bool1)+' and '+str(bool2) + ' = ' + str(bool1 and bool2))
bool1 = False
bool2 = True
print(str(bool1)+' and '+str(bool2) + ' = ' + str(bool1 and bool2))
bool1 = False
bool2 = False
print(str(bool1)+' and '+str(bool2) + ' = ' + str(bool1 and bool2))

#or
# or operator: numeric3 = numeric1 or numeric2
bool1 = True
bool2 = True
print(str(bool1)+' or '+str(bool2) + ' = ' + str(bool1 or bool2))
bool1 = True
bool2 = False
print(str(bool1)+' or '+str(bool2) + ' = ' + str(bool1 or bool2))
bool1 = False
bool2 = True
print(str(bool1)+' or '+str(bool2) + ' = ' + str(bool1 or bool2))
bool1 = False
bool2 = False
print(str(bool1)+' or '+str(bool2) + ' = ' + str(bool1 or bool2))

#not
# not operator: numeric3 = numeric1 not numeric2
bool1 = True
bool2 = False
print('not '+str(bool1) + ' = ' + str(not bool1))
print('not '+str(bool2) + ' = ' + str(not bool2))
print("==============================================================================")

