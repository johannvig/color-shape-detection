
import cv2
import numpy as np
import pyttsx3


def couleur_shape(font = cv2.FONT_HERSHEY_COMPLEX):
    
    

    # Capturing webcam footage
    cap = cv2.VideoCapture(0)


    while True:
        _, frame = cap.read()  # Reading webcam footage
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format


        # Identify the center of the screen
        height, width, _ = frame.shape
        cx = int(width / 2)
        cy = int(height / 2)

        # Pick pixel value and look at the hue of the pixel. The hue goes to 0 to 180
        pixel_center = hsv[cy, cx]
        hue_value = pixel_center[0]



        color = "Undefined"
        if hue_value ==0:
            color = "BLACK"
            
            lower_red = np.array([0,0,0])
            upper_red = np.array([250,255,30])
        elif hue_value < 5:
            color = "RED"
           
            lower_red = np.array([0, 150, 50])
            upper_red = np.array([10, 255, 255])
        elif hue_value < 22:
            color = "ORANGE"
            
            lower_red = np.array([15,150,0])
            upper_red = np.array([25,255,255])
        elif hue_value < 33:
            color = "YELLOW"
            
            lower_red = np.array([25,150,50])
            upper_red = np.array([35,255,255])
        elif hue_value < 78:
            color = "GREEN"
            
            lower_red = np.array([45,150,50])
            upper_red = np.array([65,255,255])
        elif hue_value < 131:
            color = "BLUE"
            
            lower_red = np.array([95,150,0])
            upper_red = np.array([125,255,255])
        elif hue_value < 170:
            color = "VIOLET"
            
            lower_red = np.array([155, 38, 50])
            upper_red = np.array([10, 255, 255])
        elif 170 <hue_value < 180:
            color = "PINK"
            
            lower_red = np.array([145,150,0])
            upper_red = np.array([155,255,255])

        else:
            color = "WHITE"
            
            lower_red = np.array([0,0,255])
            upper_red = np.array([0,0,255])

        print(color)

        #take the pixel HSV
        pixel_center_bgr = frame[cy, cx]

        #b is the  hue of the pixel
        #g is the saturation with values in (0,255)
        #r is the value (or Brightness)
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        #point where the pixel is taken
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)






        mask = cv2.inRange(hsv, lower_red, upper_red)  # Masking the image to find our color. The color that we want will be in white and the other colors in black.

        image2 = cv2.bitwise_and(frame, frame, mask=mask)  # Masking the image to only show our color

        # make the mask cleaner with less contours detection to focus more on the main object
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel)

        # detect the object by the contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            # approximate the contours to have the right number of points
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

            # the caracteristic of the object (color and the geometric form) will follow it on the screen
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            # only draw the contour if the object has more than 4OOpx
            if area > 400:
                # make a contour around the object with 5px
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 3:
                    # show on the screen the text with the geometric form and the color
                    cv2.putText(frame, color + "triangle", (cx - 100, 50), 0, 1, (b, g, r), 2)


                elif len(approx) == 4:

                    cv2.putText(frame, color + "Rectangle", (cx - 100, 50), 0, 1, (b, g, r), 2)
                elif len(approx) == 5:

                    cv2.putText(frame, color + "Pentagon", (cx - 100, 50), 0, 1, (b, g, r), 2)
                # if they are between 10 and 20 contours it's a circle
                elif 10 < len(approx) < 20:

                    cv2.putText(frame, color + "Circle", (cx - 100, 50), 0, 1, (b, g, r), 2)

        cv2.imshow("mask image", mask)  # Displaying mask image

        cv2.imshow("window", frame)  # Displaying webcam image

        cv2.imshow('image2', image2) #Display an image to only show the color of the shape

        cv2.waitKey(1)




couleur_shape()
