import cv2

# Global variables to store coordinates
coords = []

def click_event(event, x, y, flags, params):
    global coords
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append((x, y))
        print(f"Coordinate added: ({x}, {y})")
        # Draw a circle to mark the point
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("image", img)

# Load the image
img = cv2.imread('your_skull_image.jpg') # Replace with your image path

if img is not None:
    cv2.imshow("image", img)
    # Set mouse callback event
    cv2.setMouseCallback("image", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"All coordinates: {coords}")
else:
    print("Error: Image not found or could not be read.")

