import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)
# cv.waitKey(0)

# 1. Paint the image a certain color
blank[:] = 0,255,0   # blank[:] iterates each element of the matrix and assigns RGB value of green
# cv.imshow('Green', blank)
# cv.waitKey(0)

# 1.b. Paint only a section of the image (draw manually a square)
blank[200:300, 300:400] = 0,0,255  # Vertical pixels from 200-300 and horizontal from 300-400
# cv.imshow('Red Square', blank)
# cv.waitKey(0)

# 2. Draw a rectangle
img = cv.imread('OpenCV/Resources/Photos/Cat.jpg')
cv.rectangle(img, (330,50), (610,350), (255,0,0), thickness=2) # Rectangle draw only borders
# cv.rectangle(img, (330,50), (610,360), (255,0,0), thickness=cv.FILLED) # cv.FILLED same as -1
cv.imshow('Rectangle', img)
cv.waitKey(0)

# 3. Draw a circle
cv.circle(img, (470,220), 130, (255,0,170), thickness=4)
cv.imshow('Circle', img)
cv.waitKey(0)

# 4. Draw a line
cv.line(img, (50,400), (300,50), (255,255,255), thickness=1)
cv.line(img, (50,50), (300,400), (255,255,255), thickness=1)
cv.imshow('Line', img)
cv.waitKey(0)

# 5. Write text on an image
cv.putText(img, 'This is a cat', (360,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
cv.imshow('Text', img)
cv.waitKey(0)
