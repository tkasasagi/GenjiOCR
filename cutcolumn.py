from os import listdir
from skimage import io
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

directory = "page_data/"

save_directory = "column/"

filename = "3902.jpg"

r_thredhold = 0.03
c_thredhold = 0.02

figsize1 = 20
figsize2 = 10

#Open image file

im = io.imread(directory + filename)
plt.figure(figsize=(30, 28))
plt.imshow(im, cmap = 'gray')

v_hist = (im < 25).mean(axis=1)

plt.figure(figsize=(figsize1, figsize2))
plt.plot(v_hist)

#Get location where the block start and end

index = np.where(v_hist > r_thredhold)

start = index[0][0]  - 50
end   = index[0][-1] + 50

#get location of each column
c_hist = (im < 25).mean(axis=0)

plt.figure(figsize=(figsize1, figsize2))


for i in range(c_hist.shape[0]):
    if (c_hist[i] < c_thredhold):
        c_hist[i] = 0
    
c_hist = c_hist[np.where(c_hist > 100)]
c_hist = c_hist[np.where(c_hist < 2100)]

plt.plot(c_hist)

from scipy.signal import find_peaks_cwt

# This finds all the peaks in the distribution. Actually works really really well.
peaks = find_peaks_cwt(c_hist, np.arange(5, 50))
peaks = peaks[np.where(peaks > 100)]
peaks = peaks[np.where(peaks < 2100)]
"""
print(peaks)

plt.figure(figsize=(30, 30))
plt.imshow(im > 25, cmap = "gray")
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
    mini_hist = v_hist[left:right]
    
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
    vert_hist = (im[border:-border, mini_hist_left:mini_hist_right, :] > 25)
    
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
"""





































