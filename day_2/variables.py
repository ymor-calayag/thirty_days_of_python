import math
# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py

# Write a python comment saying 'Day 2: 30 Days of python programming'

# Declare a first name variable and assign a value to it
first_name = "Jeffrey Ymor"
print(len(first_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
quotient = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total)
print(diff)
print(product)
print(quotient)
print(remainder)
print(exp)
print(floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# A = pir**2
# C = 2pir
print("--------------------------")
r = int(input("Input radius: "))
area_of_circle = math.pi * (r**2)
circum_of_circle = 2 * math.pi * r
print(f"area of circle: {area_of_circle}")
print(f"circumference of a circle: {circum_of_circle}")
print("--------------------------")

# Declare a last name variable and assign a value to it
last_name = "Calayag"

# Declare a full name variable and assign a value to it
full_name = "Jeffrey Ymor V. Calayag"

# Declare a country variable and assign a value to it
country = "Philippines"

# Declare a city variable and assign a value to it
city = "San Fernando"

# Declare an age variable and assign a value to it
age = 30
print(type(age))

# Declare a year variable and assign a value to it
year = "2025"

# Declare a variable is_married and assign a value to it
is_married = True
print(type(is_married))

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variable on one line
spouse_first_name, spouse_last_name = "Katrina Anne", "Lubiano"
print(spouse_first_name, spouse_last_name)
print(type(spouse_first_name))