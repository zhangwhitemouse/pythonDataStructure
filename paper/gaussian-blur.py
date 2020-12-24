import cv2
from PIL import Image
import numpy as np




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

def gauss_blur(img, ksize, sigma):
    '''
    高斯模糊
    :param img: 原始图片
    :param ksize: 高斯内核大小。 ksize.width和ksize.height可以不同，但​​它们都必须为正数和奇数，也可以为零
    :param sigma: 标准差，如果写0，则函数会自行计算
    :return:
    '''
    # 外部调用传入正整数即可,在这里转成奇数
    k_list = list(ksize)
    kw = (k_list[0] * 2) + 1
    kh = (k_list[1] * 2) + 1
    resultImg = cv2.GaussianBlur(img, (kw, kh), sigma)
    return resultImg


img = cv2.imread('gray2.png')
resultImg = gauss_blur(img, (3, 3), 0)
cv2.imshow('111',resultImg)
cv2.imwrite('source_temp.png',resultImg)

src = "E:\pycharm\pythonDataStructure\paper\source_temp.png"
dst = "E:\pycharm\pythonDataStructure\paper\source2.png"
AddNoise(src,dst)
cv2.waitKey(0)
cv2.destroyAllWindows()