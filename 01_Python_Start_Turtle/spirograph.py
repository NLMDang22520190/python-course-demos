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

# The number of circles to draw
num_circles = 36

# -------------------------------------------------------------------
# Focus: For Loops and Iteration
# A 'for' loop lets us repeat a block of code a specific number of times.
# Here, 'range(num_circles)' generates numbers from 0 up to 35.
# The variable 'i' will take each of these values, one by one.
# -------------------------------------------------------------------
for i in range(num_circles):
    # Set a color based on the current step 'i'
    # colorsys.hsv_to_rgb creates a smooth rainbow gradient easily
    hue = i / num_circles
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pen.color(color)
    
    # Draw one circle
    pen.circle(100)
    
    # Turn the turtle right slightly before drawing the next circle
    # 360 degrees divided by the number of circles ensures it completes a full round
    turn_angle = 360 / num_circles
    pen.right(turn_angle)

# Keep the window open until the user clicks on it
print("Drawing complete! Click on the window to exit.")
screen.exitonclick()
