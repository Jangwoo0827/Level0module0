import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    a = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    a.shape('turtle')
    a.pensize(10)
    # Set your turtle's speed using .speed(2)
    a.speed(1000000000000000000000)
    a.shape('arrow')
    # Set your turtle's color using .color('green') and .pencolor('blue')
    a.color('blue')
    a.pencolor('gray')
    # Move your turtle forward using .forward(100)

    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    a.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    a.begin_fill()
    for i in range(4):
        a.forward(30)
        a.left(90)
    a.end_fill()
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    a.penup()
    a.goto(150, 150)
    a.pendown()
    # x=0 and y=0 is the center of the screen
    x=0
    y=0
    # Have your turtle draw a circle using .circle(radius, steps=30)
    a.begin_fill()
    a.circle(radius=20, steps=20)
    a.end_fill()
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle

    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    a.penup()
    a.goto(50, 50)
    a.pendown()
    a.begin_fill()
    for i in range(3):
        a.left(120)
        a.forward(30)
    a.end_fill()
    a.begin_fill()
    a.penup()
    a.goto(250, 10)
    a.pendown()
    a.begin_fill()
    for i in range(6):
        a.left(60)
        a.forward(20)
    a.end_fill()
    a.penup()
    a.goto(20, 100)
    a.pendown()
    a.begin_fill()
    for i in range(7):
        a.left(51.4285714286)
        a.forward(20)
    a.end_fill()


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
