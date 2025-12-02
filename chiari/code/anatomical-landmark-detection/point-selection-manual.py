import cv2
import os
import glob
import os.path as path
import json

# Global variables to store points and current image name
points = []
current_image_name = ""
output_file = "coordinates.txt"

def click_event(event, x, y, flags, param):
    """
    Mouse callback function to record coordinates on left-click.
    """
    global points, current_image_name

    if event == cv2.EVENT_LBUTTONDOWN:
        # Append the new point to the list
        points.append((x, y))
        print(f"Point added: ({x}, {y}) for image {current_image_name}")

        # Draw a small circle to visualize the selected point
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Image Point Selection", image)

def process_images_in_folder(folder_path):
    """
    Iterates through images in a folder, allows point selection, 
    and saves coordinates to a file.
    """
    global points, current_image_name, image
    data_list = []
    # Open the output file in append mode
    with open(output_file, "a") as f:
        # Find all images in the folder (supports jpg and png)
        image_files = glob.glob(os.path.join(folder_path, '*.jpg')) + \
                      glob.glob(os.path.join(folder_path, '*.png'))
        
        if not image_files:
            print(f"No images found in {folder_path}")
            return

        for img_path in image_files:
            current_image_name = os.path.basename(img_path)
            points = [] # Reset points list for each new image
            
            # Load the image
            image = cv2.imread(img_path)
            if image is None:
                print(f"Error loading image {current_image_name}. Skipping.")
                continue

            # Create a window and set the mouse callback
            cv2.namedWindow("Image Point Selection", cv2.WINDOW_NORMAL)
            cv2.setMouseCallback("Image Point Selection", click_event)

            print(f"\nProcessing image: {current_image_name}. Click points. Press 'n' to go to next image, 'ESC' to exit.")
            
            while True:
                cv2.imshow("Image Point Selection", image)
                k = cv2.waitKey(1) & 0xFF

                # Press 'n' to move to the next image
                if k == ord('n'):
                    break
                # Press 'ESC' to exit the entire process
                elif k == 27:
                    cv2.destroyAllWindows()
                    return
            json_dict = {
                  "image_name": f"{current_image_name}"}
            #      "first_coords": f"{points[0][0]}, {points[0][1]}",
            #      "second_coords": f"{points[1][0]}, {points[1][1]}"
            # }
            # data_list.append(item)
            # Write the collected points to the file
           # json_output = json.dumps(data_list, indent=4)

           # print(json_output)
            json_string = json.dumps(json_dict)
            data = json.loads(json_string)
            count = 0
            for point in points:
                 if(count == 0 ):
                    new_data = {"first_coords": f"{point[0]}, {point[1]}"}
                    data.update(new_data)
                    count = count +1
                 elif(count == 1):
                    new_data = {"second_coords": f"{point[0]}, {point[1]}"}
                    data.update(new_data)

                 
            updated_json_string = json.dumps(data, indent=4)
            #f.write(f"  ({point[0]}, {point[1]})\n")
            f.write(f"{updated_json_string}\n")
            #f.write(f"Image: {current_image_name},")
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # Specify the path to your folder containing images
    #images_folder_path = "../../images" 
    images_folder_path =  path.abspath(path.join(__file__ ,"../../../images"))
    # Clear the output file before starting a new session
    if os.path.exists(output_file):
        os.remove(output_file)

    process_images_in_folder(images_folder_path)
    print(f"\nCoordinates saved to {output_file}")
