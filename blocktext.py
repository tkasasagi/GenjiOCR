from skimage import io
from scipy import ndimage
import sys

import matplotlib.pyplot as plt

image_file = "binarization2/200003803_00002.jpg"
file_extension = image_file.split(".")[-1]

im = ndimage.imread(image_file)

print(im)

# plot the amount of white ink across the columns & rows
row_vals = list([sum(r) for r in im  ])
col_vals = list([sum(c) for c in im.T])

# plot the column (x-axis) pixel dilations
plt.plot(col_vals)
plt.show()

# plot the row (y-axis) pixel dilations
plt.plot(row_vals)
plt.show()

from skimage import filters, segmentation

# apply the mask to the image object
clean_border = segmentation.clear_border(im)

# plot the resulting binarized image
plt.imshow(clean_border, cmap='gray')
plt.show()


from skimage.measure import label

# labeled contains one integer for each pixel in the image,
# where that image indicates the segment to which the pixel belongs
labeled = label(clean_border)

from skimage.measure import regionprops

# create array in which to store cropped articles
cropped_images = []

# define amount of padding to add to cropped image
pad = 20

# for each segment number, find the area of the given segment.
# If that area is sufficiently large, crop out the identified segment.
for region_index, region in enumerate(regionprops(labeled)):
  if region.area < 2000:
    continue

  # draw a rectangle around the segmented articles
  # bbox describes: min_row, min_col, max_row, max_col
  minr, minc, maxr, maxc = region.bbox

  # use those bounding box coordinates to crop the image
  cropped_images.append(im[minr-pad:maxr+pad, minc-pad:maxc+pad])

import os

# create a directory in which to store cropped images
out_dir = "segmented_articles/"
if not os.path.exists(out_dir):
  os.makedirs(out_dir)

# save each cropped image by its index number
for c, cropped_image in enumerate(cropped_images):
  io.imsave( out_dir + str(c) + ".png", cropped_image)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  