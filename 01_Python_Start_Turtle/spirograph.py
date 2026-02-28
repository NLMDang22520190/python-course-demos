import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Geometric Spirograph")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)  # 0 is the fastest speed
pen.width(2)
pen.hideturtle()  # Hide the turtle cursor for faster drawing

# -------------------------------------------------------------------
# Focus 1: Functions
# A function is a reusable block of code. We define it once and can
# call it with different parameters to get different results.
# -------------------------------------------------------------------
def draw_spirograph(num_loops, radius, color_shift_speed):
    """Draws a colorful spirograph based on given parameters."""
    
    # -------------------------------------------------------------------
    # Focus 2: For Loops and Iteration
    # The 'for' loop repeats a block of code 'num_loops' times.
    # -------------------------------------------------------------------
    for i in range(num_loops):
        # Calculate a unique color for each step using the HSV color model
        hue = (i * color_shift_speed) / num_loops
        
        # Using colorsys to convert Hue, Saturation, Value to RGB format
        # ensure hue stays between 0.0 and 1.0 using the modulo operator (%)
        color = colorsys.hsv_to_rgb(hue % 1.0, 1.0, 1.0)
        pen.color(color)
        
        # Draw the shape (a circle)
        pen.circle(radius)
        
        # Turn the turtle right slightly before drawing the next circle
        # 360 degrees divided by num_loops ensures it completes a full round perfectly
        turn_angle = 360 / num_loops
        pen.right(turn_angle)

# Now we call the function!
# We can easily change these numbers to completely alter the final drawing
print("Drawing started...")
draw_spirograph(num_loops=72, radius=120, color_shift_speed=2.5)

# Keep the window open until the user clicks on it
print("Drawing complete! Click on the window to exit.")
screen.exitonclick()
