import numpy as np
from skimage.data import imread
import matplotlib.pyplot as plt


image_file = "dataset2/200003803_00087.jpg"

im = imread(image_file)

#print(im)

plt.figure(figsize=(30, 20))
plt.imshow(im, cmap='gray')

shape = im.shape
print(shape)


v_hist = (im < 25).mean(axis=0).mean(axis=1)


plt.figure(figsize=(30, 20))
plt.plot(v_hist)


index = np.where(v_hist == (np.max(v_hist)))
print(index[0])

        
from PIL import Image
from os import listdir

directory = "genjidata/image/"

file_list = listdir(directory)



#Crop and save
dim = (250, 500, 5000, 3550)

crop_img = im[0:shape[0], int(index[0]):int(shape[1])]

plt.figure(figsize=(30, 20))
plt.imshow(crop_img, cmap='gray')




for i in range(len(file_list)):
    image = Image.open((directory + file_list[i]))

    crop_img = image.crop(dim)

    crop_img.save("dataset/" + file_list[i])
    
    image.close()


























# plot the amount of white ink across the columns & rows
#row_vals = list([sum(r) for r in im  ])
col_vals = list([sum(c) for c in im.T])

# plot the column (x-axis) pixel dilations
plt.figure(figsize=(20, 10))
plt.plot(col_vals)
plt.show()

# plot the row (y-axis) pixel dilations
##plt.show()

from scipy.signal import find_peaks_cwt

peaks = find_peaks_cwt(col_vals, np.arange(10, 500))
print(peaks)

plt.figure(figsize=(10, 10))
plt.imshow(im > 25)
for peak in peaks:
    plt.axvline(x=peak)
plt.show()


# The really complicated code for bounding boxes

peak_borders = []
shape = im.shape

# Parameters
border = 10 # Ignore N pixels from the left
hist_max = 0.985 # Threshold for detection. hist_max=0.99 means at least 1% of the row/column needs to be black for it to be considered "containing text"
buffer = 5 # Add N pixels to the bounding box in each direction, just to make sure it surrounds the text

# Repeat for every peak we found above
for i in range(len(peaks)):
    # First, we try to find the horizontal boundary of the column (where it starts and ends)
    
    # If this is the first peak, then we start the search space `border` pixels into the image, ignoring the edges of the image
    # Otherwise, we start the search halfway between this peak and the last peak
    # We need to segment the image initially like this to make sure each bounding box only has one column.
    # Likewise, we end the search halfway between the peak and the next peak
    if i == 0:
        left = border
    else:
        left = np.ceil((peaks[i] + peaks[i - 1]) / 2).astype(int)
   
    if i == (len(peaks)) - 1:
        right = shape[1] - border
    else:
        right = np.floor((peaks[i] + peaks[i + 1]) / 2).astype(int)
        
    print(left, right)
        
    # Crop the vertical histogram based on the boundaries set above.
    mini_hist = col_vals[left:right]
    
    # Plot the boundaries. You can see in the plot the histogram dips below the threshold when text is present in the image
    # It can be confusing because 0=black and 1=white, so a value of 1 means no text present.
    plt.plot(mini_hist)
    plt.title('Peak {} horizontal'.format(i))
    plt.axhline(y=hist_max, color='red')
    plt.show()

    # Now this finds the actual left and right borders of the text
    # The left boundary is the first column of pixels to have more than 1.5% black pixels (text)
    # The right boundary is the last column of pixels to have more than 1.5% black pixels
    # 5px buffer is also added to the bounding box on each side
    mini_hist_left = left + (mini_hist < hist_max).argmax() - buffer
    mini_hist_right = left + len(mini_hist) - (mini_hist[::-1] < hist_max).argmax() + buffer
    
    # Now the variables mini_hist_left and mini_hist_right have the left and right boundaries of the column
    
    # Crop the image between the new left and right borders and make another histogram but vertically
    vert_hist = (im[border:-border, mini_hist_left:mini_hist_right, :] > -25).mean(axis=1).mean(axis=1)
    
    # Repeat the same as was done horizontally, but instead find the first and last pixel rows to contain more than 1.5% text
    # This gives us the top and bottom boundaries for the bounding box
    
    plt.plot(vert_hist)
    plt.title('Peak {} vertical'.format(i))
    plt.axhline(y=hist_max, color='red')
    plt.show()
    
    mini_hist_top = border + (vert_hist < hist_max).argmax() - buffer
    mini_hist_bottom = border + len(vert_hist) - (vert_hist[::-1] < hist_max).argmax() + buffer
    
    # Done!
    peak_borders.append((mini_hist_left, mini_hist_right, mini_hist_top, mini_hist_bottom))



import matplotlib.patches as patches

#plt.figure(figsize=(10, 10))
fig,ax = plt.subplots(1, figsize=(10, 10))
plt.imshow(im)
for l, r, t, b in peak_borders:
    #plt.axvline(x=l, color='blue')
    #plt.axvline(x=r, color='red')
    rect = patches.Rectangle((l, t),r - l,b - t,linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
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
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  