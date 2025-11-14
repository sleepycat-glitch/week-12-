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

# add more characters [keeps giving errors so don't uncomment]
# new_list = list(range(12, 120))
# list.extend(new_list)
# print(list(range(12, 120)))
# new_list2 = list(range(120, 200))
# list.extend(new_list2)
# print(list)

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
#.reverse() reverses order of list

# why is list more efficient than variables?
# list can hold multiple values while variable can only hold one
# more organized and able to access multiple items from one container
# able to change values

cakes = ["chocolate", "vanilla", "red velvet", "carrot"]
print(cakes)
cakes[0] = "strawberry" # changes item at index 0 to another
print(cakes)
cakes.append("lemon")
print(cakes)
cakes[1] = "chocolate"
print(cakes)
cakes.pop() # only removes last item
print(cakes)
cakes.insert(2, "funfetti") # inserts at index 2
print(cakes)


# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']


my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
foods = ["pozole", "fish and rice", "spaghetti and chicken", "tamales", "curry"]
# Print the second and last item.
print(foods[1])
print(foods[-1])
# Add a new item using .append().
foods.append("sushi")
# Remove the first item using .pop(0).
foods.pop(0)
# Reverse your list using .reverse().
print(foods[::-1])
# Create a list of 3 lists (matrix), and access the middle element.
all = [foods, numbers, cakes]
print(all[1])

# sets are unordered collections of unique items
# sets do not support indexing or slicing
# sets are mutable, meaning you can add or remove items
# sets use curly braces
# no duplicate items for sets

my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
my_set.add(6) # adds item to set
print(my_set)
my_set.remove(3) # removes item from set
print(my_set)
print(4 in my_set) # true
print(3 in my_set) # false

# tuples are ordered collections of items
# immutable, cannot modify them after creation
# created using parentheses
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])

