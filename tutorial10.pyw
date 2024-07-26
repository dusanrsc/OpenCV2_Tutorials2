# importing module
import cv2
import numpy

# loading image
img = cv2.imread("assets/ronaldo.jpg")
img2 = cv2.imread("assets/soccer_practice.jpg")

# resizing image cuz it is to large
resized_img2 = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)

# basic image info
#print(img.shape)	# returns (number of rows, columns and channels)
#print(img.size)		# returns (total number of pixels)
#print(img.dtype)	# returns (data types) useful for debugging

# spliting image by channels
blue, green, red = cv2.split(img)

# merging last splited image 
img = cv2.merge((blue, green, red))

### NOTE: THIS METHOD IS CALLED ROI REGION-OF-INTEREST 
# slicing ball from image and storing it in variable
ball = img[400:500, 190:270]

### NOTE: MUST BE SAME SIZE AS SLICED IMAGE
# placing sliced ball on the image
img[400:500, 0:80] = ball

### NOTE: BOTH IMAGES MUST BE SAME SIZE
# resizing images by pixels rows and columns
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

### NOTE: BOTH IMAGES MUST BE SAME SIZE
# method for molding two images
combined_img = cv2.add(img, img2)

# method for adding weight to images (transparency level)
waighted_img = cv2.addWeighted(img, 0.4, img2, 0.6, 0)

# displaying image
cv2.imshow("Tutorial10", waighted_img)

# not allow window to close
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()