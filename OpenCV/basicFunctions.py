import cv2 as cv
import numpy as np

img = cv.imread('OpenCV/Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)


# 1. Convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale cat', gray)


# 2. Blur
blur = cv.GaussianBlur(img, (7,7), 0, borderType = cv.BORDER_DEFAULT)
# cv.imshow('Blurry cat', blur)


# 3. Edge Cascade (Canny Edges)
canny = cv.Canny(img, 125, 175,)
cannyBlur = cv.Canny(blur, 125, 175, edges = 4)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
# cv.imshow('Canny edges', canny)
# cv.imshow('Canny soft edges', cannyBlur)


# 4. Dilating an image based on a structuring element, 
dilated = cv.dilate(cannyBlur, np.ones((3,3)), iterations=1)
# dilate = cv.dilate(cannyBlur, (3,3), iterations=3)
# cv.imshow('Dilated softer edges', dilated) 


# 5. Eroding an image (opposite of dilating)
eroded = cv.erode(dilated, (3,3), iterations=2)
# cv.imshow('Eroded softer edges', eroded)


# 6. Adding two images
addedEdges = cv.add(canny, dilated)
# cv.imshow('Both tipes of edges', addedEdges) # Paint the two different edges on same image


# 7. Subtracting two images
subtractedEdges = cv.subtract(dilated, cannyBlur)
# # cv.imshow('Subtracted', subtractedEdges)


# 8. Resize
resized = cv.resize(img, (500,500))
# # cv.imshow('Resized', resized)


# 9. Crop
cropped = img[55:340, 340:605]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
