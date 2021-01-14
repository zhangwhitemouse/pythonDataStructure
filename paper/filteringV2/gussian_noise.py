import skimage
import cv2


origin = cv2.imread("E:\Masters\pic\\railpic\IMG_4329.JPG")
noisy = skimage.util.random_noise(origin, mode='gaussian', var=0.01)
cv2.namedWindow("noise",0)
cv2.resizeWindow("noise",1200,800)
cv2.imshow("noise",noisy)
# cv2.imwrite("noise_01.png",noisy*255)
cv2.waitKey(0)
cv2.destroyAllWindows()