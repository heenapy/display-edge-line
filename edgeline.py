import cv2
import numpy as np
image = cv2.imread('pqr.png')
orig_image=image.copy()
cv2.imshow('input image', image)
#_____________edge line display________
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)
cv2.imshow('canny edges',edged)
cv2.waitKey()

contrours , hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('canny edges after contrours image',edged)
print(contrours)
print('number of contours found=' + str(len(contrours)))

cv2.drawContours(image,contrours,-1 ,(0,255,0),3)
cv2.imshow('contours',image)