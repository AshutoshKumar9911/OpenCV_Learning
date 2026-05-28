import cv2
image = cv2.imread("Image Resizing & Shaping/Learning_OpenCV.png")

if image is None:
  print("could not load the image")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original_image" , image)
    cv2.imshow("flipped_Horizontal" , flipped_horizontal)
    cv2.imshow("flipped_Vertical" , flipped_vertical)
    cv2.imshow("flipped_Both" , flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
