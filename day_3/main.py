# Declare your age as integer variable
age = 29
# Declare your height as a float variable
height = 1.62
# Declare a variable that store a complex number
complex_num = 1j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("----------------------")
base_of_triangle = int(input("Input base: "))
height_of_triangle = int(input("Input height: "))
area_of_triangle = 0.5 * base_of_triangle * height_of_triangle
print(f"area of triangle: {area_of_triangle}")
print("----------------------")
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
print("----------------------")
side_a = int(input("Side A of triangle: "))
side_b = int(input("Side B of triangle: "))
side_c = int(input("Side C of triangle: "))
perimeter = side_a + side_b + side_c
print(f"perimeter of a triangle: {perimeter}")
print("----------------------")
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("----------------------")
rect_length = int(input("length: "))
rect_width = int(input("width: "))
rect_area = rect_length * rect_width
rect_perimeter = (2 * (rect_length + rect_width))
print(f"rectangle area: {rect_area}")
print(f"rectangle perimeter: {rect_perimeter}")
print("----------------------")
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("----------------------")
word_one = len("python")
word_two = len("dragon")
print(word_one != word_two)
print('on' in "python" and 'on' in "dragon")
print("----------------------")
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("----------------------")
print('jargon' in "I hope this course is not full of jargon")
print("----------------------")
# There is no 'on' in both dragon and python
print("----------------------")
print('on' not in "python" and 'on' not in "dragon")
print("----------------------")
# Find the length of the text python and convert the value to float and convert it to string
print("----------------------")
result = str(float(len("python")))
print(result)
print("----------------------")
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("----------------------")
def is_even(num):
    return True if num % 2 == 0 else False

num = int(input("Input a number: "))
print(is_even(num))
print("----------------------")
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("----------------------")
num_one = 7 // 3
num_two = int(2.7)
print(num_one == num_two)
print("----------------------")
# Check if type of '10' is equal to type of 10
print("----------------------")
print(type('10') == type(10))
print("----------------------")
# Check if int('9.8') is equal to 10
print("----------------------")
print(True if int(float('9.8')) == 10 else False)
print("----------------------")
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
print("----------------------")
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate}")
print("----------------------")
# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years = int(input("Enter number of years you have lived: "))
years_to_seconds = (((years * 365) * 24) * 60) * 60
print(f"You have lived for {years_to_seconds}.")
print("----------------------")
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print("----------------------")
print("1 1 1 1 1")
for i in range(2, 6):
    print(i, 1, i, i**2, i**3)
print("----------------------")