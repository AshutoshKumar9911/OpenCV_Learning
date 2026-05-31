import cv2

image = cv2.imread("Image Drawing Function/Learning_OpenCV.png")

if image is None:
  print("Oops! Your image is not working")
else:
  print("Image loaded successfully")
  
  cv2.circle(image,(150,150),50,(255,0,0),-1)

  cv2.imshow("edited image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


  