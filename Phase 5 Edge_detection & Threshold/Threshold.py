import cv2

image = cv2.imread("Phase 5 Edge_detection & Threshold/a house in mountain.png",cv2.IMREAD_GRAYSCALE)

ret, thresh_image = cv2.threshold(image,120,255,cv2.THRESH_BINARY)


cv2.imshow("Original_Image",image)
cv2.imshow("threshold_image",thresh_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
