import cv2

img = cv2.imread("E:\Masters\pic\exp\p200.JPG", 0)
cv2.namedWindow("img", 0)
cv2.resizeWindow("img", 1200, 800)
cv2.imshow("img",img)
cv2.imwrite('img.png', img)
# x = cv2.Sobel(img, cv2.CV_16S, 1, 0)  # 1,0代表只计算x方向计算边缘
# y = cv2.Sobel(img, cv2.CV_16S, 0, 1)  # 0,1代表只在y方向计算边缘
# absX = cv2.convertScaleAbs(x)
# cv2.namedWindow("x", 0)
# cv2.resizeWindow("x", 1200, 800)

# absY = cv2.convertScaleAbs(y)
# cv2.namedWindow("y", 0)
# cv2.resizeWindow("y", 1200, 800)
# dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
# cv2.imshow("x", absX)
# cv2.imshow("y", absY)
# cv2.imwrite('sobel_x.png', absX)
# cv2.imwrite('sobel_y.png', absY)
# cv2.imwrite('sobel.png', dst)
# cv2.imshow("res", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
