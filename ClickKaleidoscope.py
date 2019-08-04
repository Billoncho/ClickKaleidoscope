# ClickKaleidoscope.py
# Billy Ridgeway
# Creates a kaleidoscope of spirals where ever the
# screen is clicked.

import random               # Imports the random library.
import turtle               # Imports turtle library.
t = turtle.Pen()            # Creates a new turtle pen called t.
t.speed(0)                  # Sets the speed of the pen to fast.
t.hideturtle()              # Hides the pen.
turtle.bgcolor("black")     # Sets the background color to black.

# Creates a list of colors.
colors = ["red", "yellow", "blue", "green", "orange", "purple",
          "white", "gray"]

# Defines our kaleidoscopt function using spirals
def draw_kaleido(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    draw_spiral(x,y, size)      # Calls the draw spiral function.
    draw_spiral(-x,y, size)     # Calls the draw spiral function.
    draw_spiral(-x,-y, size)    # Calls the draw spiral function.
    draw_spiral(x,-y, size)     # Calls the draw spiral function.

# Defines a function to draw a spiral of a certain size and location.
def draw_spiral(x,y, size):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(92)

turtle.onscreenclick(draw_kaleido) # Calls the draw kaleido function.
        
    


            
