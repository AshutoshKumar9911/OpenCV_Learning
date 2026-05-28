import cv2

image = cv2.imread("Image Resizing & Shaping/Learning_OpenCV.png")

if image is not None:
  cropped = image[100:200 , 50:150]
  cv2.imshow("original",image)
  cv2.imshow("cropped_image",cropped)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
