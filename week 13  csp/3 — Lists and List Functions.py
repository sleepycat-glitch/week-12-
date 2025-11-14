# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collections family in python

list = [1,2,3,4,5]
print(list)
print(len(list)) # 5
print(type(list)) # class = list
print(list[0]) # 1
print(list[1:4]) # 2,3,4
print(list[:-1]) # 1,2,3,4
print(list[::-1]) # reverses list 

list.extend([6,7,8,9,10,11]) # adding multiple variables to list 
# list. append(6) only adds one item to list
print(list)
list.pop(2) # removes item at index 2
print(list)
list.sort() # sorts them in ascending order
print(list)
list.reverse() # also reverses
print(list)
list.pop(-1) # removes item at last index
print(list)

# add more characters
new_list = range(12:120)
list.extend(new_list)
print(list)


new_list2 = list[range(120:200)]
list.extend(new_list2)
print(list)
print(list[::3]) # prints every third number
print(list[::10])

del list[::3]
print(len(list))
print(list)



# list functions:
#.append() adds an item to end of list
#.extend() adds multiple items to list
#.pop() removes and reutrns item at given index
#.remove() removes first occurrence of specific value
#.sort() sorts list in ascending order
#.reverse() reverses order of lsit





# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']


# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
# foods = ["pozole", "fish and rice", "spaghetti and chicken", "tamales", "curry"]
# # Print the second and last item.
# print(foods[1] [4])
# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.