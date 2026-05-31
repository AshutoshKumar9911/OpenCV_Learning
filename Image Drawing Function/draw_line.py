import cv2
image = cv2.imread("Image Drawing Function/Learning_OpenCV.png")

if image is None:
  print("Oops! your image is not working")
else:
  print("image loaded successfully")

  h,w,c = image.shape
  print(f"Image Loaded:\n Height:{h}\n width:{w}\nChannels:{c}")

  pt1 = (50,100)
  pt2 = (300,100)

  color = (255,0,0)
  thickness = 4

  cv2.line(image,pt1,pt2,color,thickness)
  
  cv2.imshow("Line Draw", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
