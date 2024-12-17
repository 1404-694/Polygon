import turtle
# Importing library

# Setting up the screen
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)

# Defining the turtle
polygon = turtle.Turtle() 

# Defining variables
num_sides = 6  # Number of sides
side_length = 70
angle = 360.0 / num_sides

# Iterating loop for total number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

# Completing the drawing
turtle.done()
