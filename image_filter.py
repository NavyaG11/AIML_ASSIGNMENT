import cv2

# Load image
image = cv2.imread(r'C:\Users\USER\Desktop\AI assignments\sample.jpg')

# Check if image loaded
if image is None:
    print("Error: Image not found. Check path!")
    exit()

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(image, (7, 7), 0)

# Edge Detection
edges = cv2.Canny(image, 100, 200)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()