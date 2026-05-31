import cv2

image = cv2.imread("Image Drawing Function/Learning_OpenCV.png")

if image is None:
  print("Oops! Your image is not working")
else:
  print("Image loaded successfully")
  
  cv2.putText(image,"Hello World Champions",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),2)
  cv2.imshow("Adding text over image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


  