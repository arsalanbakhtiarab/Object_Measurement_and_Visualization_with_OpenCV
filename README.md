**Object Measurement and Visualization with OpenCV**

This Python script allows you to measure and visualize objects in an image using the OpenCV library. The script performs the following tasks:

1. **Zoom Out**: It resizes the image to zoom out, allowing a better view of objects.

2. **Object Detection**: The script converts the resized image to grayscale and applies Otsu's thresholding to create a binary image. It then detects contours to identify objects in the image.

3. **Dimension Calculation**: For each detected object, the script calculates its width and height in millimeters (assuming a conversion rate of 1 pixel = 0.1 mm).

4. **Visualization**: The top 3 objects closest to the center of the image are selected and displayed. The script draws rectangles around the objects and annotates their dimensions on the image.

**Usage**:
1. Set the `zoom_out_scale` to control the zoom level of the image.
2. Modify the `layer` variable (0 to 4) to adjust object width and height measurements based on the layer.
3. Replace `path` with the file path of the image you want to analyze.
4. Run the script to visualize the objects with their measurements.

**Note**: Adjust the `pixels_per_mm` variable based on the image resolution for accurate dimension measurements.

Feel free to use this script for various applications, such as analyzing object sizes and positions in different images. Contributions and improvements are welcome.

**Requirements**:
- Python 3.x
- OpenCV library (cv2)
- NumPy library (numpy)
