# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment (assigning values), while == is comparison (comparing values).

a = 3
b = 4
print(a) #output = 3
print(b) #output = 4

print(a == b)   # False, checks for equality
print(a != b)   # True, checks if not equal to 
print(a > b)    # False, checks if greater than
print(a < b)    # True, checks if less than
print(a >= b)   # False, checks if greater than or equal to
print(a <= b)   # True, checks if less than or equal to 


#predict the output of the following comparisons:
10 > 5  # true
7 == 2 * 3 + 1 # true
8 != 8 # false
4 <= 2 + 2 # true

# Write 3 examples that result in True and 3 that result in False.
c = 5
d = 10
print(c<d) 
print(c*2==d) 
print(d!=c)

print(d<c)
print(d==c)
print(d<=c)

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
score = int(input("What was your test score?: "))
# make program for all grading spectrums
# grade = 100 - 90, A
# grade = 89-80, B
# grade = 79-70, C
# grade = 69-61, D
# grade = below 60, F
if score>=60:
    print("You passed the test.")

else:
    print("You did not pass the test.")


grade = int(input("What is your current grade?: "))

if grade<=60:
    print("Your current grade is a F.")
else:
    if grade<=69:
        print("Your current grade is a D.")
    else:
        if grade<=79:
            print("Your current grade is a C.")
        else:
            if grade<=89:
                print("Your current grade is a B.")
            else:
                print("Your current grade is an A.")

# & = and operator
# | = or operator
# ^ = or operator
# ~ = not operator

# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
password = input("What is your password?: ")
print(password.find())

