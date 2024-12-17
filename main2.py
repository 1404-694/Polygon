import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("Aqua")

# Set up the turtle
board = turtle.Turtle()

# Draw the first triangle for the star
board.forward(100)  # Draw base
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

# Position for the second triangle
board.penup()
board.right(150)
board.forward(50)

# Draw the second triangle for the star
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)

# To keep the window open until the user closes it
screen.mainloop()