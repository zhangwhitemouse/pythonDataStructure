import numpy as np
import cv2


# 一维高斯函数
def Gaussian(x, sigma=1.0):
    result = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(x / sigma) ** 2 / 2)
    return result


# 二维高斯函数
def Gaussian2D(x, y, sigmaX=1.0, sigmaY=1.0):
    result = Gaussian(x, sigmaX) * Gaussian(y, sigmaY)
    return result


# 一维高斯卷积核
def GaussianKernel(length, sigma=None):
    radius = length // 2
    kernel = np.zeros(length, dtype=np.float32)
    if sigma is None:
        sigma = 0.3 * ((length - 1) * 0.5 - 1) + 0.8
    for i in range(length):
        kernel.itemset(i, Gaussian(i - radius, sigma=sigma))
    # 归一化
    sum = np.sum(kernel)
    kernel = kernel / sum
    return kernel


# 二维高斯卷积核
def GaussianKernel2D(ksize, sigmaX=None, sigmaY=None):
    kernelX = GaussianKernel(ksize[0], sigmaX).reshape(ksize[0], 1)
    kernelY = GaussianKernel(ksize[1], sigmaY).reshape(1, ksize[1])
    kernel = kernelX * kernelY
    k = 1 / kernel[0, 0]
    kernel = np.int32(kernel * k + 0.5)
    return kernel


# 二维高斯卷积核
def GetGaussianKernel2D(ksize, sigmaX=None, sigmaY=None):
    if sigmaX is None:
        sigmaX = 0.3 * ((ksize[0] - 1) * 0.5 - 1) + 0.8
    if sigmaY is None:
        sigmaY = 0.3 * ((ksize[1] - 1) * 0.5 - 1) + 0.8
    kernelX = cv2.getGaussianKernel(ksize[0], sigmaX).reshape(ksize[0], 1)
    kernelY = cv2.getGaussianKernel(ksize[1], sigmaY).reshape(1, ksize[1])
    kernel = kernelX * kernelY
    k = 1 / kernel[0, 0]
    kernel = np.int32(kernel * k + 0.5)
    return kernel


# 优化的高斯滤波
def GaussianFilter(src, ksize):
    # 卷积分离
    kernelX = GaussianKernel(ksize[0])
    kernelX = np.resize(kernelX, (ksize[0], 1))
    kernelY = GaussianKernel(ksize[1])
    kernelX = np.resize(kernelX, (1, ksize[1]))
    dst = cv2.filter2D(src, -1, kernelX)
    dst = cv2.filter2D(dst, -1, kernelY)
    return dst


if __name__ == '__main__':
    src = cv2.imread('noise_005.png')
    cv2.namedWindow("src",0)
    cv2.resizeWindow("src", 1200, 800)
    dst = GaussianFilter(src, (5, 5))
    cv2.namedWindow("dst", 0)
    cv2.resizeWindow("dst", 1200, 800)
    cv2.imshow('src', src)
    cv2.imwrite("src2.png",src)
    cv2.imshow('dst', dst)
    cv2.imwrite("dst2.png", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
