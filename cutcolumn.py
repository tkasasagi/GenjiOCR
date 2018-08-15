from os import listdir
from skimage import io
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

directory = "page_data/"

save_directory = "column/"

filename = "004.jpg"

r_thredhold = 0.03
c_thredhold = 0.03

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
plt.plot(c_hist)

from scipy.signal import find_peaks_cwt

# This finds all the peaks in the distribution. Actually works really really well.
peaks = find_peaks_cwt(c_hist, np.arange(20, 60))
peaks




