import cv2

# Load the image (use correct path)
image = cv2.imread(r"download2.jpeg")

# Check if image loaded
if image is None:
    print("❌ Error: Image not found. Check path or file name.")
else:
    # Create resizable window
    cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Loaded Image', 400, 500)

    # Show image
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print image properties
    print("Image Dimensions:", image.shape)