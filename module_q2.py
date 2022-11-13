# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area


length = input('What is the length of your house? ')
width = input('What is the width of your house? ')
sqft = int(length) * int(width)
print(f'Your house is {sqft} square feet. ')



# 2) Has a function to calculate the circumference of a circle 
# Program in Jupyter Notebook should take in user input and use imported functions to 
# calculate a circle's circumference or a houses square footage

radius = input("What is the radius of the circle in inches? ")
pi = 3.14159265359
circumference = 2 * pi * int(radius)
print(f'The circumference of the circle is {round(circumference, 1)} inches.')