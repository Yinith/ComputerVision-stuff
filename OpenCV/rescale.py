import cv2 as cv

# Re-scaling
def rescaleFrame(frame, scale=0.75):
    # Works for images, videos, and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeRes(capt, width, height):
#     # Works for live video only?
#     capt.set(3,width)
#     capt.set(4,height)


# Re-scale an image
img = cv.imread('OpenCV/Resources/Photos/cat_large.jpg')
cv.imshow('Cat', rescaleFrame(img, 0.50))
cv.waitKey(0)

# Re-scale a video
capture = cv.VideoCapture('OpenCV/Resources/Videos/dog.mp4')
isTrue, frame = capture.read()
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

