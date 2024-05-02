import cv2 as cv

# Contours are the boundaries of objects, the curve that joins the continuous points along the boundary of an object.
# They are useful for shape analysis and object detection and recognition.
# From a mathematical point of view, contours are not the same as edges.

img = cv.imread('OpenCV/Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    # RETR_TREE for all the hierarchical contours
    # RETR_EXTERNAL for only external contours
    # RETR_LIST for all the contours in the image



cv.waitKey(0)