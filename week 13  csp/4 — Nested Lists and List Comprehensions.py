# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
# print(groceries[0][0]) #apple
# # #similar to coordinate system: first [] is row, second [] is column
# print(groceries[1][2])
# print(groceries[2][2])
# print(groceries[2][1])
# print(groceries[2][0])

#nested list
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

#nested loop
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()





# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
# simpler version of nested loop
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

matrix1 = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

# Print the first list.
print(matrix1[0])
# Print the second item from the third list.
print(matrix1[2][1])
# Use a list comprehension to extract the last item from each sub-list.
first_col1 = [row[-1] for row in matrix1]
print(first_col1)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.

squares = [x**2 for x in range(1,11)]
print(squares)