import numpy as np
import cv2 as cv

def canny(image, low_threshold, high_threshold):
    return cv.Canny(image, low_threshold, high_threshold)


image = cv.imread('E:\Masters\pic\paper\\track.jpg',0)
can = canny(image,40,130)
# cv.imwrite("canny.png",can)
cv.namedWindow("canny",0)
cv.resizeWindow("canny",1200,800)
cv.imshow("canny",can)
cv.waitKey(0)
cv.destroyAllWindows()