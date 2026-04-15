import cv2

# Load image
image = cv2.imread('sample.jpg')   # keep image in same folder

# Print shape
print("Shape of image:", image.shape)

# Height, Width, Channels
height, width, channels = image.shape
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

# Print some pixel values
print("\nPixel value at (0,0):", image[0, 0])
print("Pixel value at center:", image[height//2, width//2])