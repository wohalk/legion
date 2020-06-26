import cv2

img = cv2.imread('1.jpg')
img1 = cv2.imread('2.jpg')
print(img1.shape)
img1 = cv2.resize(img1,(300,300))
print(img.shape)

img = cv2.resize(img,(300,300))
img2 = cv2.addWeighted(img,0.5,img1,0.5,5)

cv2.imshow('xx',img)
cv2.imshow('lk',img1)
cv2.imshow('togeth',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


