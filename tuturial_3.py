import numpy as np
import cv2 as cv

def extract_object():
    capture = cv.VideoCapture(r"C:\Users\sprin\Desktop\practicePy\vid\VID_20200223_204904.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb = lower_hsv, upperb = upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c == 27:
            break

print("--------Hello Python !--------")
src = cv.imread(r"C:\Users\sprin\Desktop\practicePy\img\Hog.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

extract_object()
'''b, g, r = cv.split(src)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

src = cv.merge([b, g, r])
src[:, :, 0] = 0
cv.imshow("changed", src)'''

cv.waitKey(0)
cv.destroyAllWindows()