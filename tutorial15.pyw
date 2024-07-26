# importing modules
import cv2
import numpy

# loading image from memory into program
img = cv2.imread("assets/newspaper.jpg", 0)

# simple techniques
# of threshold(imageVariable, thrasholdValueA, thrasholdValueB, thrasholdMethod)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# advanced techniques of thrashold(imageVariable, maxValue, addaptiveMethod, thrasholdType, blockSize, valueOfC)
threshold2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
threshold3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# displaying images
cv2.imshow("Tutorial15", img)

cv2.imshow("threshold", threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("threshold3", threshold3)

# standard methods
cv2.waitKey(0)
cv2.destroyAllWindows()