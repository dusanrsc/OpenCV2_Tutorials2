# importing modules
import cv2
import numpy

# loading image from memory into program
img = cv2.imread("assets/gradient.jpg", 0)

# simple techniques of threshold(imageVariable, thrasholdingValueA, thrasholdingValueB, thrasholdingMethod)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, threshold2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, threshold3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, threshold4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, threshold5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# displaying images
cv2.imshow("Tutorial14", img)
cv2.imshow("Threshold" , threshold)
cv2.imshow("Threshold2", threshold2)
cv2.imshow("Threshold3", threshold3)
cv2.imshow("Threshold4", threshold4)
cv2.imshow("Threshold5", threshold5)

# standard methods
cv2.waitKey(0)
cv2.destroyAllWindows()