import cv2
image=cv2.imread("dog.jpg")
gray_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted=255-gray_img
blurred=cv2.GaussianBlur(inverted,(21,21),0)
invertedblur=255-blurred
pencilsketch=cv2.divide(gray_img,invertedblur, scale=256.0)

cv2.imwrite("dog1.jpg", pencilsketch)