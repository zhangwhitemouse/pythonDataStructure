import cv2

image = cv2.imread('E:\Masters\pic\paper\\rail2.jpg', cv2.IMREAD_GRAYSCALE)
maxval = 255
otsuThe = 0
otsuThe, dst_Otsu = cv2.threshold(image, otsuThe, maxval, cv2.THRESH_OTSU)
cv2.namedWindow("Otsu",0)
cv2.resizeWindow("Otsu",1200,800)
cv2.imshow('Otsu', dst_Otsu)
# cv2.imwrite('Otsu2.png',dst_Otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()