from PIL import Image, ImageDraw

def draw_mcrae_line(image_path, output_path, basion_coords, opisthion_coords):
    """
    Draws the McRae line on a specified image.

    Args:
        image_path (str): Path to the input medical image (e.g., 'skull_xray.jpg').
        output_path (str): Path to save the output image with the line drawn.
        basion_coords (tuple): (x, y) coordinates for the basion (anterior foramen magnum).
        opisthion_coords (tuple): (x, y) coordinates for the opisthion (posterior foramen magnum).
    """
    try:
        # Open the image
        img = Image.open(image_path).convert("RGB")
        draw = ImageDraw.Draw(img)

        # Define the color and width for the line
        line_color = (255, 0, 0)  # Red color (RGB)
        line_width = 2

        # Draw the line
        # The line connects the basion to the opisthion
        draw.line([basion_coords, opisthion_coords], fill=line_color, width=line_width)

        # Save the modified image
        img.save(output_path)
        print(f"McRae line drawn and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Placeholder coordinates (example only, adjust for your specific image):
# Assuming basion is at (100, 250) and opisthion is at (400, 250)

basion_x = 100
basion_y = 250
opisthion_x = 400
opisthion_y = 250

draw_mcrae_line(
    image_path='skull_xray.jpg',
    output_path='skull_xray_mcrae_line.jpg',
    basion_coords=(basion_x, basion_y),
    opisthion_coords=(opisthion_x, opisthion_y)
)
