

# 中值滤波#
import cv2
import numpy as np
from PIL import Image


def AddNoise(src, dst, probility=0.05, method="salt_pepper"):
    imarray = np.array(Image.open(src))
    height = imarray.shape[0]
    width = imarray.shape[1]

    for i in range(height):
        for j in range(width):
            if np.random.random(1) < probility:
                if np.random.random(1) < 0.5:
                    imarray[i, j] = 0
                else:
                    imarray[i, j] = 255
    new_im = Image.fromarray(imarray)
    new_im.save(dst)


def MedianFilter(img,k=3,padding=None):
    imarray=img
    height = imarray.shape[0]
    width = imarray.shape[1]
    if not padding:
        edge = int((k - 1) / 2)
        if height - 1 - edge <= edge or width - 1 - edge <= edge:
            print("The parameter k is to large.")
            return None
        new_arr = np.zeros((height, width), dtype="uint8")
        for i in range(edge,height-edge):
            for j in range(edge,width-edge):
                new_arr[i, j] = np.median(imarray[i - edge:i + edge + 1, j - edge:j + edge + 1])# 调用np.median求取中值
    return new_arr



# src = "E:\pycharm\pythonDataStructure\paper\gray.png"
# dst = "E:\pycharm\pythonDataStructure\paper\gray_noise.png"
# AddNoise(src,dst)
img = cv2.imread("gray_noise.png", 0)
result = MedianFilter(img)
cv2.imwrite('middle.jpg', result)
cv2.imshow("input", img)
cv2.imshow("output", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
