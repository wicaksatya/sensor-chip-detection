import cv2
import numpy as np
import imutils

img = cv2.imread('D:\\circles.jpg',0)
img = cv2.medianBlur(img,9)
if img.shape[1] > 600:
    img = imutils.resize(img, width=400)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
edge_detected_image = cv2.Canny(cimg, 100, 200)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)