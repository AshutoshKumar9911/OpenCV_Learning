import cv2

image = cv2.imread("Phase 1/Learning_OpenCV.png")

if image is not  None:
  cv2.imshow("Image displaying ", image)# open the window 
  cv2.waitKey(0) # wait for the key to be pressed
  cv2.destroyAllWindows() # close the window
else:
  print("Could not load the image")
