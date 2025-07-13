import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3

# Voice Engine Setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Optional: change voice

# Load Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize Webcam
cap = cv2.VideoCapture(0)

# Setup GUI Window
window = tk.Tk()
window.title("Face Detection with Voice")
window.geometry("800x600")

label = tk.Label(window)
label.pack()

detected_before = False

# Function to Detect Face and Speak
def detect_face():
    global detected_before

    # Capture frame from webcam
    ret, frame = cap.read()
    if not ret:
        return

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If faces are found and voice not already triggered
    if len(faces) > 0 and not detected_before:
        engine.say("Face detected")
        engine.runAndWait()
        detected_before = True
    elif len(faces) == 0:
        detected_before = False

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert image to RGB (OpenCV to Tkinter)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=img_pil)

    label.imgtk = imgtk
    label.configure(image=imgtk)

    # Repeat function every 10 milliseconds
    label.after(10, detect_face)

# Start the loop
detect_face()
window.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()
