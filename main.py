import cv2
import numpy as np

# Set the zoom out scale
zoom_out_scale = 0.20

# Layer # 0
 
# layer = 0
# path = r'\images\ANMP0075.jpg'

# Layer # 1

# layer = 1
# path = r'\images\ANMP0076.jpg'

# Layer # 2

# layer = 2
# path = r'\images\ANMP0077.jpg'

# Layer # 3

# layer = 3
# path = r'\images\ANMP0078.jpg'

# Layer # 4

layer = 1
path = r'\images\ANMP0107.jpg'

# Load the image
image = cv2.imread(path)

# Resize the image to zoom out
resized_image = cv2.resize(image, None, fx=zoom_out_scale, fy=zoom_out_scale)

# Convert the resized image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
_, binary_image = cv2.threshold(
    gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(
    binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour at the center of the image
center_x = resized_image.shape[1] // 2
center_y = resized_image.shape[0] // 2

# Create a list to store the objects' distances from the center
object_distances = []

# Loop over each detected contour
for contour in contours:
    # Calculate the distance from the contour centroid to the image center
    moments = cv2.moments(contour)
    if moments["m00"] != 0:  # Avoid division by zero
        contour_centroid_x = int(moments["m10"] / moments["m00"])
        contour_centroid_y = int(moments["m01"] / moments["m00"])
        distance = np.sqrt((contour_centroid_x - center_x) **
                           2 + (contour_centroid_y - center_y) ** 2)

        # Add the contour distance to the list
        object_distances.append((distance, contour))

# Sort the objects by their distances from the center
object_distances.sort(key=lambda dist: dist[0])

# Get the dimensions of the three objects closest to the center
top_3_objects = object_distances[:1]

# Set the position for drawing lines and text
line_start_x = 10
line_start_y = 50
line_length = 100
line_spacing = 40

# Draw lines, rectangles, and annotate dimensions for the top 3 objects
for i, (distance, contour) in enumerate(top_3_objects):
    # Calculate the dimensions of the object in pixels
    x, y, w, h = cv2.boundingRect(contour)

    # Calculate the dimensions of the object in millimeters
    # Assuming 1 pixel = 0.1 mm (adjust this value according to your image)
    # pixels_per_mm = 1 / 0.1
    pixels_per_mm = 4.0
    print("Pixels_per_mm :", pixels_per_mm)
    object_width_mm = w / pixels_per_mm
    object_height_mm = h / pixels_per_mm

    # object_width_mm = Temp_object_width_mm
    print('object_width_mm:', object_width_mm)
    print('object_height_mm:', object_height_mm)
    if layer == 0:
        object_height_mm = object_height_mm + 4
        object_width_mm = object_width_mm + 4
    elif layer == 1:
        object_height_mm = object_height_mm + 1
        object_width_mm = object_width_mm + 1
    elif layer == 2:
        object_height_mm = object_height_mm 
        object_width_mm = object_width_mm
    elif layer == 3:
        object_height_mm = object_height_mm -2
        object_width_mm = object_width_mm -2
    elif layer == 4:
        object_height_mm = object_height_mm - 4
        object_width_mm = object_width_mm - 4

    # Draw the bounding rectangle with the dimension on the edge of the object
    color = (0, 255, 0)  # Green color
    cv2.rectangle(resized_image, (x, y), (x + w, y + h), color, 2)

    # Draw a line from left to right
    line_start = (x, y + h // 2)
    line_end = (x + w, y + h // 2)
    cv2.line(resized_image, line_start, line_end, (255, 0, 0), 2, cv2.LINE_AA)

    # Draw a line from top to bottom
    line_start = (x + w // 2, y)
    line_end = (x + w // 2, y + h)
    cv2.line(resized_image, line_start, line_end, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.line(resized_image, (line_start_x, line_start_y),
             (line_start_x + line_length, line_start_y), color, 2)
    cv2.putText(resized_image, "Width : {:.2f}mm".format(object_width_mm),
                (line_start_x + line_length + 10, line_start_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Add space between the lines
    line_start_y += line_spacing

    cv2.line(resized_image, (line_start_x, line_start_y),
             (line_start_x + line_length, line_start_y), color, 2)
    cv2.putText(resized_image, "Length : {:.2f}mm".format(object_height_mm),
                (line_start_x + line_length + 10, line_start_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    line_start_y += line_spacing

# Display the image with measurements
cv2.imshow("Image with Measurements", resized_image)
# cv2.imshow("Binary Image",binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
