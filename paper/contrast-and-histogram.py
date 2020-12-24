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
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(img)
    # res = np.hstack((img, equ))
    return equ


src = 'E:\\pycharm\\pythonDataStructure\\paper\\gray.png'
contrast_img = contrast(src)
histogram_img = histogram(src)
cv2.imshow("C-Output", contrast_img)
cv2.imshow("H-Output", histogram_img)
# cv2.imwrite('contrast.png')
cv2.waitKey(0)
cv2.destroyAllWindows()


