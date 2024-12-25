# # Exercise: Functions in python
# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```

def calculate_area(base, height):
    return (1/2)*base*height


# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(base, height, shape='triangle'):
    if shape == 'triangle':
        return (1/2)*base*height
    elif shape == 'rectangle':
        return base*height
    else:
        return "Invalid shape type"

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(n):
    if n == 3:
        s=""
        for i in range(1, n+1):
            s += '*'
            print(s)
    elif n == 4:
        for i in range(1, n+1):
            print('*'*i)
    else:
        print("Invalid number")


n=input("Enter a number: ")

print_pattern(int(n))
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/10_functions/10_functions_exercise.py)