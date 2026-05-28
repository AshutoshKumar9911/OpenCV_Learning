import cv2
 
image = cv2.imread("Phase 1/Learning_OpenCV.png")

if image is not None:
  success = cv2.imwrite("World_Cup.png",image)
  if success:
    print("Image saved successfully as 'World_Cup.png'")
  else:
    print("Failed to save  an image")
else:
  print("Error: Could not load an image")
