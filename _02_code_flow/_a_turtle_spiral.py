import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    import turtle
    
    # This code sets our shape to a turtle
    c = turtle
    c.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    c.speed(0)
    # Set your turtle's color using .color('green')
    c.color('blue')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        # Set the turtle color to a random color
        c.color(get_random_color())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        c.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        c.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        c.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
