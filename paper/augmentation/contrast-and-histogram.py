import cv2
import numpy as np

def contrast(src):
    img = cv2.imread(src)
    xp = [0, 64, 128, 192, 255]
    fp = [0, 16, 128, 240, 255]
    x = np.arange(256)
    table = np.interp(x, xp, fp).astype('uint8')
    img = cv2.LUT(img, table)
    return img

def histogram(src):
    img = cv2.imread(src)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(img1)

    cv2.equalizeHist(channels[0],channels[0])
    cv2.merge(channels,img1)
    cv2.cvtColor(img1,cv2.COLOR_YCR_CB2BGR,img)
    # res = np.hstack((img, equ))
    return img


src = 'E:\Masters\pic\\railpic2\IMG_4519.JPG'
# contrast_img = contrast(src)
# cv2.namedWindow("con",0)
histogram_img = histogram(src)
cv2.namedWindow("his",0)
# cv2.resizeWindow("con",1200,800)
cv2.resizeWindow("his",1200,800)
# cv2.imshow("con", contrast_img)
cv2.imshow("his", histogram_img)
# cv2.imwrite('contrast.png',contrast_img)
cv2.imwrite('histogram.png',histogram_img)
cv2.waitKey(0)
# cv2.destroyAllWindows()


