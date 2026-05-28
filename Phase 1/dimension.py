import cv2
image = cv2.imread("Phase 1/Learning_OpenCV.png")

if image is not None:
  h,w,c = image.shape
  print(f"Image Loaded:\n Height:{h}\n width:{w}\nChannels:{c}")
else:
  print("Could not load an image")
