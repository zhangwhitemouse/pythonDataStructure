import numpy as np
import cv2

img = cv2.imread(r'src2.png')
img_mean = cv2.blur(img, (5,5))

img_median = cv2.medianBlur(img, 5)

cv2.imwrite('avg2.png', img_mean)
cv2.namedWindow('avg',0)
cv2.resizeWindow('avg',1200,800)
cv2.imshow('avg', img_mean)

cv2.imwrite('med2.png', img_median)
cv2.namedWindow('med',0)
cv2.resizeWindow('med',1200,800)
cv2.imshow('med', img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()