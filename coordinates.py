//this code gives average of all black points coordinates (using pixel....)
import numpy as np
import cv2

img = cv2.imread('Desktop/img3.jpg')

x, y, z = np.where(img == (0, 0, 0))
points = list(zip(x, y))

if points:
    points_array = np.array(points)
    average_x = np.mean(points_array[:, 0])
    average_y = np.mean(points_array[:, 1])
    print("Average X coordinate:", average_x)
    print("Average Y coordinate:", average_y)
else:
    print("No points found with the specified color.")
