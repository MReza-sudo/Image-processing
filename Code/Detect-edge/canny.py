import cv2
import numpy as np
# Load the image
img = cv2.imread("image1.jpg")
img = cv2.resize(img, dsize=(500, 500), interpolation=cv2.INTER_CUBIC)
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detection algorithm
edges = cv2.Canny(gray, 100, 300)

# Convert the image to a matrix
matrix = np.array(img)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Scharr
scharrx = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(gray, cv2.CV_64F, 0, 1)

# Laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Show the original image and the edges
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
# cv2.imshow("Edges_Sobelx", sobelx)
# cv2.imshow("Edges_Sobely", sobely)
# cv2.imshow("Edges_Scharrx", scharrx)
# cv2.imshow("Edges_Scharry", scharry)
# cv2.imshow("Edges_laplacian", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
