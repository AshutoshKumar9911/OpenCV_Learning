import cv2

image = cv2.imread("Phase 1/Learning_OpenCV.png")

if image is None:
  print("Error: Image is not found")
else:
  print("Image load successfully")
