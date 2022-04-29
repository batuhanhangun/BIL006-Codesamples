#Character and String objects
# '<some_characters>' or "<some_characters>" denotes a string


string1 = 'Artificial' 
print(string1)
#You can also use "". Generally, Python users tend to use single quotes (' ') for identifiers and use double quotes (" ") for messages and string interpolation.
string2 = "Intelligence"
print(string2)
print("string1: " + string1)
print("string2: " + string2)

#Concatenating string objects
# + operator: String3 = "String1" + "String2"
string3 = "String1" + "String2"
print(string3)
print("string3: " + string3)
string3 = string1 + string2
print(string3)
print("string3: " + string3)


#Better to add some space to make it more appealing
string3 = string1 + " " + string2
print(string3)
print("string3: " + string3)
print("==============================================================================")

print("==============================================================================")
print("Swapping values between two objects")

#NOTE: There is a more efficient and easy to use way to create formatted string by using the string literals called as f-string
# http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

#Swapping values between two string objects
print("\nValues of string1 and string2 before swap")
print('string1: " + string1)
print('string2: " + string2)
string1, string2 = string2, string1
print("\nValues of string1 and string2 after swap")
print("string1: " + string1)
print("string2: " + string2)
print("==============================================================================")

print("==============================================================================")
print("Accesing any character in a string")
#Accesing any character in a string
print("string3[4]: "  + string3[4])
print("==============================================================================")

