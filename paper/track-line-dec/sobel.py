import cv2
import numpy as np

img = cv2.imread("E:\Masters\pic\paper\\track.jpg", 0)
x = cv2.Sobel(img,cv2.CV_16S,1,0)  #1,0代表只计算x方向计算边缘
y = cv2.Sobel(img,cv2.CV_16S,0,1)  #0,1代表只在y方向计算边缘
absX = cv2.convertScaleAbs(x)

absY = cv2.convertScaleAbs(y)
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)
# cv2.imshow("absX", absX)
# cv2.imshow("absY", absY)
cv2.namedWindow("x",0)
cv2.resizeWindow("x",1200,800)
cv2.imwrite('sobel.png',dst)
cv2.imshow("x", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()