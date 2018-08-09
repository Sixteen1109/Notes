# -- coding: utf-8 --
import cv2

img = cv2.imread('img.jpg')

cv2.imshow('XDDDDD',img)

img2 = cv2.imread('img.jpg',0)
#好
cv2.imshow('XDDDDDD',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
