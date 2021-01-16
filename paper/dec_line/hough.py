# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img = cv2.imread('E:\Masters\pic\exp\p200.JPG')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像
# blur_gray = cv2.GaussianBlur(gray, (15, 15), 0, 0)
# edges = cv2.Canny(blur_gray,10,100)
# plt.subplot(121),plt.imshow(edges,'gray')
# plt.xticks([]),plt.yticks([])
#
# #hough transform
# lines = cv2.HoughLinesP(edges,1,np.pi/180,30,minLineLength=60,maxLineGap=15)
# lines1 = lines[:,0,:]#提取为二维
# for x1,y1,x2,y2 in lines1[:]:
#     cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)
#
# plt.subplot(122),plt.imshow(img,)
# plt.xticks([]),plt.yticks([])
# plt.show()


import cv2 as cv
import numpy as np
import matplotlib as plt

# read image and check
filename = "E:\Masters\pic\exp\p200.JPG"
img = cv.imread(filename)
img_p = img.copy() #用于显示概率Hough变换的检测结果

if img is None:
    print("Image read error!")
else:
    print("Image read successful!")
# cv.imshow("Source", img)

# image space change from BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# threshold
# _, binary = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
_, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
# cv.imshow("Threshold", binary)

# edges detection with Canny method
edges = cv.Canny(binary, threshold1=50, threshold2=200)
# cv.imshow("Canny", edges)

# HoughLines()函数
lines = cv.HoughLines(edges, rho = 1, theta = 1 * np.pi/180, threshold=120, srn=0, stn = 0, min_theta=1, max_theta=2)

for i in range(0, len(lines)):
    rho, theta = lines[i][0][0], lines[i][0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.namedWindow("Hough_line",0)
cv.resizeWindow("Hough_line",1200,800)
cv.imshow("Hough_line", img)

# HoughLinesP()函数
lines_p = cv.HoughLinesP(edges, rho = 1, theta = np.pi/180, threshold = 50, minLineLength= 30, maxLineGap=10)

for i in range(len(lines_p)):
    x_1, y_1, x_2, y_2 = lines_p[i][0]
    cv.line(img_p, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)

print("code successful!")
cv.namedWindow("Hough_line_p",0)
cv.resizeWindow("Hough_line_p",1200,800)
cv.imshow("Hough_line_p", img_p)
cv.imwrite("Hough_line.png",img_p)

cv.waitKey(0)
cv.destroyAllWindows()
