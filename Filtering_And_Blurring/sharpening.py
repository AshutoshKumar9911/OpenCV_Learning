import cv2
import numpy as np

image = cv2.imread("Filtering_And_Blurring\WIN_20250327_16_17_41_Pro.jpg")

sharpen_kernel = np.array([
  [0,-1,0],
  [-1,5,-1],
  [0,-1,0]
])

sharpened = cv2.filter2D(image,-1,sharpen_kernel)

cv2.imshow("Original image",image)
cv2.imshow("sharpened_image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
