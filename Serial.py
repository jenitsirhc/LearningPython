# Image processing - Sharpening an image
import cv2
import time

start = time.perf_counter()
# Load the original image
image = cv2.imread("images/Rickroll.jpg")
# Resize the image
img = cv2.resize(image, (500, 600))
# To show original image
cv2.imshow('Original Image', img)
# To blur the image
bimage = cv2.blur(image, (20, 20))
# Resize the image
img = cv2.resize(bimage, (500, 600))
# To display the blurred image
cv2.imshow('blurred Image', img)
# To save the blurred image
cv2.imwrite('images/blurredImage.jpg',bimage)
# Waits for a pressed key
cv2.waitKey(0)
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s))")