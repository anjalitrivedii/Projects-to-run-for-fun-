import turtle
from PIL import Image

# Load and resize image
image_path = "C:\\Users\\anjal\\Downloads\\28306-thumb-360-0.jpg"  # Replace with your image path
img = Image.open(image_path)
img = img.resize((50, 50))  # Resize to reduce drawing time
img = img.convert("RGB")  # Convert gto RGB

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

dot_size = 10  # Size of each dot
spacing = 12  # Space between dots

# Draw image using dots
for y in range(img.height):
    for x in range(img.width):
        r, g, b = img.getpixel((x, y))
        t.goto(x * spacing - img.width * spacing / 2, img.height * spacing / 2 - y * spacing)
        t.dot(dot_size, (r / 255, g / 255, b / 255))  # Normalize RGB to [0, 1]

turtle.done()
