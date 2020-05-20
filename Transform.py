src="Box5-A1-27-01-11500.tif" #extract from xml files
a =[-12.4219340480873,1.02329692936977,0.0547410605730517,0,0,0]
b =[6.70121729036356,-0.345509738706612,0.972479703389782,0,0,0]

from PIL import Image
import numpy as np
from tifffile import imread, imsave, imshow
import matplotlib.pyplot as plt
from math import *
import numpy as np
from matplotlib.patches import Circle


img = imread(src)
img = np.flip(img.T, 1)
imshow(img)

#affine transform
t_img = np.zeros((6000, 5000)) #hard coded for now but will depend on image size
t_points = []
print(img.shape[0])
print(img.shape[1])
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        result_x = a[0] + a[1]*x + a[2]*y
        result_y = b[0] + b[1]*x + b[2]*y
        t_img[round(result_x)][round(result_y)] = img[x][y]
        t_points.append(result_y)
# print(min(t_points))
imshow(t_img)

#inverse affine transform
epsilon = 5e-10;
it_img = np.zeros((10000, 10000)) #hard coded for now but will depend on image size
for x in range(t_img.shape[0]):
    for y in range(t_img.shape[1]):
        u = x - a[0];
        v = y - b[0];
        p = a[1]*b[2] - a[2]*b[1];
        if ( fabs(p) > epsilon ):
            result_x = (b[2]*u - a[2]*v)/p;
            result_y = (a[1]*v - b[1]*u)/p;
        it_img[round(result_x)][round(result_y)] = t_img[x][y]
imshow(it_img)
