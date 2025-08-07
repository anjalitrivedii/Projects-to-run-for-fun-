import cv2
import numpy as np

# Load the images
foreground = cv2.imread("C:\\Users\\anjal\\Downloads\\28306-thumb-360-0.jpg")  # Image with green screen
background = cv2.imread("C:\\Users\\anjal\\Downloads\\coffee-shop-counter-with-blank-coffee-cup-mockup-for-hot-beverages-free-photo.jpg")     # New background image

# Check if files were loaded successfully
if foreground is None:
    print("❌ Error: 'greenscreen_image.jpg' not found or can't be read.")
    exit()

if background is None:
    print("❌ Error: 'new_background.jpg' not found or can't be read.")
    exit()

# Resize background to match foreground
background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

# Convert image to HSV
hsv = cv2.cvtColor(foreground, cv2.COLOR_BGR2HSV)

# Define green color range in HSV
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Create mask to detect green
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Extract non-green parts from the foreground
fg_no_green = cv2.bitwise_and(foreground, foreground, mask=mask_inv)

# Extract green parts from background
bg_green_parts = cv2.bitwise_and(background, background, mask=mask)

# Combine both images
final = cv2.add(fg_no_green, bg_green_parts)

# Show result
cv2.imshow("Green Screen Replaced", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
