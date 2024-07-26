# importing modules
import cv2
import numpy

# image section
# creating black image
img = numpy.zeros((250, 500, 3), numpy.uint8)

# creating black image with white rectangle
img = cv2.rectangle(img, (200, 0), (300, 100), (255, 255, 255), -1)

# loading black and white image
img2 = cv2.imread("assets/black_white.jpg")

### NOTE: BITWISE TRUTH TABLES
############ OR ########### ########## AND ########## ########## XOR ########## ###### NOT ######
# ------------------------- ------------------------- ------------------------- -----------------
# /   A   /   B   /   Q   / /   A   /   B   /   Q   / /   A   /   B   /   Q   / /   A   /   Q   /
# ------------------------- ------------------------- ------------------------- -----------------
# /   0   /   0   /   0   / /   0   /   0   /   0   / /   0   /   0   /   1   / /   0   /   1   /
# /   0   /   1   /   0   / /   0   /   1   /   1   / /   0   /   1   /   0   / /   1   /   0   /
# /   1   /   0   /   0   / /   1   /   0   /   1   / /   1   /   0   /   0   / -----------------
# /   1   /   1   /   1   / /   1   /   1   /   1   / /   1   /   1   /   1   /
# ------------------------- ------------------------- -------------------------

# bitwise method for comparing images takes(image1, image2)
bit_and = cv2.bitwise_and(img, img2)
bit_or = cv2.bitwise_or(img, img2)
bit_xor = cv2.bitwise_xor(img, img2)

# take(image)
bit_not = cv2.bitwise_not(img)
bit_not2 = cv2.bitwise_not(img2)

# displaying images
cv2.imshow("Tutorial11", img)
cv2.imshow("Tutorial11A", img2)

cv2.imshow("BitAnd", bit_and)
cv2.imshow("BitOr", bit_or)
cv2.imshow("BitXor", bit_xor)

cv2.imshow("BitNot", bit_not)
cv2.imshow("BitNot2", bit_not2)

# not allow window to close
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()
