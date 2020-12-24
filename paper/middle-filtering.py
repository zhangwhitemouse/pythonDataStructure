

# 中值滤波#
import cv2
import numpy as np

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


img = cv2.imread("source2.png", 0)
result = MedianFilter(img)
cv2.imwrite('middle2.jpg', result)
# cv2.imshow("input", img)
cv2.imshow("output", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
