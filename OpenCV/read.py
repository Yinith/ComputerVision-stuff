import cv2 as cv

# Reading an image
# img = cv.imread('OpenCV/Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Reading a video
# capture = cv.VideoCapture('OpenCV/Resources/Videos/dog.mp4')
capture = cv.VideoCapture(0)
isTrue, frame = capture.read()
# cv.imshow('Video', frame)
# cv.waitKey(1000)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    # Show each frame for 20ms and if the letter d is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()