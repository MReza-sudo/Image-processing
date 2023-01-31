import cv2
from matplotlib import pyplot as plt

# Load the image and resize it to 512
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)

# Create a SIFT object
sift = cv2.SIFT_create()

# # Set the threshold value
# sift.setDouble('contrastThreshold', 0.5)

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(img, None)
#print(keypointsq)
# Draw the keypoints on the image
img_keypoints = cv2.drawKeypoints(img, keypoints, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show the image with keypoints
cv2.imshow("Keypoints",img_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
