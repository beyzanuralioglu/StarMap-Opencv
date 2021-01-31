##Beyzanur Alioğlu

import numpy as np
import cv2
img = cv2.imread("/home/beyzanur/Downloads/StarMap.png")
img2 = cv2.imread("/home/beyzanur/Downloads/Small_area.png")
print("beyza")
height, width, _ = img.shape
h, w, _ = img2.shape
print(w, h)
print(width, height)
leftcorner=img[0:h , 0:w]
rightcorner=img[0:h , width-w:width]
lowerleftcorner=img[height-h:height, 0:w]
lowerrightcorner=img[height-h:height , width-w:width]
rotatedsmallimage = cv2.rotate(lowerleftcorner, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("LeftCorner", leftcorner)
cv2.imshow("RightCorner", rightcorner)
cv2.imshow("RotatedCorner", rotatedsmallimage)
cv2.imshow("LowerRightCorner", lowerrightcorner)

cv2.waitKey(0)
cv2.destroyAllWindows()