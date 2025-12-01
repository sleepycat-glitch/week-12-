# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temp = int(input("What is today's temperature?(in Fahrenheit): "))
if temp<=60:
    print("cold")
elif temp<=80 and temp>60:
    print("warm")
else:
    print("hot")

if temp<-10 or temp>110:
    print("Extreme temperature warning!")