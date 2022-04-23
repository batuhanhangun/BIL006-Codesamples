#List objects
shopping_list = ['eggs', 'milk', 'chocolate', 'water']

#Basic output
print("==============================================================================")
print("Basic output")
print(shopping_list)
print("==============================================================================")

#Lenght of a list
print("==============================================================================")
print("Length of list: " + str(len(shopping_list)))
print("==============================================================================")

#Accesing any element in a list
#index starts at 0 in Python!
print("==============================================================================")
print("Accesing any item in a list")
print(shopping_list[2])
print("==============================================================================")


#Insert an element to the end of a list
# list.append(element_to_be_added)
print("==============================================================================")
print("Appending a list")
shopping_list.append('honey')
print(shopping_list)
print("==============================================================================")


#Insert an element to the specific index of a list
# list.insert(index, element_to_be_added)
print("==============================================================================")
print("Inserting an item into a specific index in a list")
shopping_list.insert(3, 'yoghurt')
print(shopping_list)
print("==============================================================================")


#Duplicate values are allowed in list
print("==============================================================================")
print("Inserting duplicate values")
shopping_list.append('honey')
print(shopping_list)
print("Length of list: " + str(len(shopping_list)))
print("==============================================================================")




#Remove element from a list
print("==============================================================================")
print("Removing an element from a list with pop()")
shopping_list.pop(len(shopping_list)-1)
print(shopping_list)
print("Length of list after pop operation: " + str(len(shopping_list)))
print("==============================================================================")



#Remove element with a specific value (only removes first occurrence)
print("==============================================================================")
print("Removing an element from a list with remove()")
shopping_list.remove('chocolate')
print(shopping_list)
print("Length of list after pop operation: " + str(len(shopping_list)))
print("==============================================================================")


#Sorting a list
print("==============================================================================")
print("Sorting a list with sort()")
shopping_list.sort()
print(shopping_list)
print("==============================================================================")

#Reversing a list
print("==============================================================================")
print("Reversing a list with reverse()")
shopping_list.reverse()
print(shopping_list)
print("==============================================================================")


#Removes all elements from a list
print("==============================================================================")
print("Removing all elements from a list with clear()")
shopping_list.clear()
print(shopping_list)
("==============================================================================")

#More information about the collection object types
# A list is an organized and changeable collection of items. Allows for the creation of duplicate members.
# Tuple is an ordered and unchanging collection. Allows for the creation of duplicate members.
# A set is an unsorted, unchangeable[1], and unindexed collection. There are no duplicate members.
# A dictionary is an ordered[2] and changing collection. There are no duplicate members.
# [1]Set items cannot be changed, however you may remove and/or add things at any time.
# [2]As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
