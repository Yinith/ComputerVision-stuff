import cv2 as cv
import numpy as np

image = cv.imread('OpenCV/Resources/Photos/park.jpg')
cv.imshow('Boston park', image)


#######   1. Translation  #################################################

def translate(img, x, y): # x,y are the number of pixels to shift the image
    # We create a translation matrix. 
    transMat = np.float32([[1,0,x],[0,1,y]])
    # The 2x3 matrix is a list of 2 lists with 3 elems each
    dimensions = (img.shape[1], img.shape[0])
    # Affine transformation applying the matrix
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(image, 50, 100)    # Image shifted 50px right and 100px down
# cv.imshow('Translated', translated)


#######   2. Rotation   ####################################################

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(image, -30, (100,500))
# cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -90)
# cv.imshow('Rotated rotated', rotated_rotated)


#######   3. Resizing   ####################################################

resized = cv.resize(image, (1000,1000), interpolation=cv.INTER_CUBIC) 
# for shrinking image, use INTER_AREA. For enlarging it's better INTER_LINEAR, best INTER_CUBIC (slower)
# cv.imshow('Resized', resized)


#######   4. Flipping / mirroring   ##########################################

flip = cv.flip(image, -1)  # flipCode: 0 = flip vertically, 1 = horizontally, -1 = both axises
cv.imshow('Flipped', flip)


#######   5. Cropping   #######################################################

cropped = flip[200:400, 100:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)