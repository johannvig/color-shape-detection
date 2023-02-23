# color-detection


This code uses computer vision to detect the color and shape of an object in real-time using a webcam. The script requires the OpenCV, Numpy, and pyttsx3 libraries to run.

The script uses pyttsx3 to give the user instructions on how to use the code. After launching the code, the user is prompted to show an object to the camera in the middle of the screen to detect the color and the shape. The code then captures footage from the webcam and converts it to the HSV format, which is better suited for color detection.

The script uses a predefined range of HSV values for each color, and based on the hue value of the pixel at the center of the screen, it determines the color of the object. The color is then used to mask the image and find the object's contours. If the object's area is larger than 400 pixels, the code draws a contour around it and detects its shape. The shape and color of the object are then displayed on the screen.

To run the code, ensure that the required libraries are installed, and run the script. Note that the script will only detect the color and shape of the object in the middle of the screen.
