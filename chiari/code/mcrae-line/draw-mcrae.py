import cv2
import numpy as np

def draw_mcrae_line(image_path, basion_coords, opisthion_coords):
    """
    Loads an image and draws the McRae line between the specified coordinates.

    Args:
        image_path (str): The path to the input image file.
        basion_coords (tuple): A tuple (x, y) for the basion point.
        opisthion_coords (tuple): A tuple (x, y) for the opisthion point.
    """
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    # Define line parameters
    color = (0, 255, 0)  # Green color in BGR
    thickness = 2

    # Draw the line
    cv2.line(img, basion_coords, opisthion_coords, color, thickness)

    # Display the image with the drawn line (optional)
    cv2.imshow("Image with McRae Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Replace 'skull_xray.png' with your image path.
# Replace (100, 200) and (400, 200) with your actual basion and opisthion coordinates.
# If using the manual method to get coordinates, those values would go here.
draw_mcrae_line('skull_xray.png', (100, 200), (400, 200))
