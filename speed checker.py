
import time

text = "Books are a window to the world. They help us explore different lives, cultures, and ideas without leaving our room."
print("Type this sentence:")
print(text)
start = time.time()
typed = input("\nStart typing: ")
end = time.time()

words = len(typed.split())
speed = words / (end - start) * 60
print("Your typing speed is:", round(speed, 2), "WPM")