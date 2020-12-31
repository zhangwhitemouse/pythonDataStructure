import numpy as np
import cv2
import glob
from matplotlib import pyplot as plt

img = cv2.imread(r'source2.png', 0)
# cv2.imshow('img', img)
img_copy = img.copy()
width = img.shape[0]  # 宽
length = img.shape[1]  # 高
kernel = 5  # 卷积核大小 / 滑动窗大小
padding = (kernel - 1) // 2  # 扩展操作，为了对原图所有的点都操作
img_new = np.zeros([width + 2 * padding, length + 2 * padding], dtype=np.uint8)  # 扩展原图，补零
# 将原图 铺在 新图上
for i in range(width):
    for j in range(length):
        img_new[padding + i, padding + j] = img[i, j]

slide_window = []  # 滑动窗的内容
for i in range(width):
    for j in range(length):
        window_sum = 0  # 滑动窗的和
        for m in range(kernel):
            for n in range(kernel):
                slide_window.append(img_new[i + m, j + n])
                window_sum += img_new[i + m, j + n]
        window_average = window_sum / len(slide_window)
        img_copy[i, j] = window_average  # 取均值
        del slide_window[:]

# print('okok---------')
cv2.imwrite('avage2.png', img_copy)
cv2.imshow('img_after', img_copy)
# print(img_copy.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

