import cv2

mri_img = cv2.imread('E:\Masters\pic\\railpic2\IMG_4519.JPG')

lab = cv2.cvtColor(mri_img, cv2.COLOR_BGR2LAB)

lab_planes = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=10,tileGridSize=(8,8))

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.namedWindow("p",0)
cv2.resizeWindow("p",1200,800)
cv2.imwrite('clahe.png', bgr)
cv2.imshow('p',bgr)
cv2.waitKey(0)
