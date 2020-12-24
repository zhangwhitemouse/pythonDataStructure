#!/usr/bin/env python
# coding: utf-8
import cv2 as cv
import matplotlib.pyplot as plt


# 图片路径
# （应避免有中文）
image_path = r'gray2.png'


# 读取图片
# 类型：numpy.ndarray
image = cv.imread(image_path)

# 显示原图
# cv.namedWindow('cat', cv.WINDOW_NORMAL)
# cv.resizeWindow('cat', 200, 200)
# cv.imshow('cat', image)
# cv.waitKey(0)

# 使用 ravel 拉直图像
# ravel：将多维矩阵降为一维矩阵
image_ravel = image.ravel()

# 显示灰度直方图
# plt.hist(image_ravel, 256, [0, 256])
plt.hist(image_ravel)

plt.show()

color = ['blue', 'green', 'red']
for i, color_sub in enumerate(color):
    # 要计算的图
    # 要计算的维度
    # 要计算的区域ROI，计算整图则为None
    # 子区段数目
    # 要计算的像素范围
    hist = cv.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color_sub)
    plt.xlim([0, 256])
plt.show()




