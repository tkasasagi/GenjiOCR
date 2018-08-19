from os import listdir
from skimage import io
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

directory = "realpages/"

save_directory = "column/"

filename = "39_4.jpg"

r_thredhold = 0.03
c_thredhold = 0.1

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

print("start at ", start, " ,end at ", end, " ,total height= ", (end - start))
#get location of each column
c_hist = (im < 25).mean(axis=0)

plt.figure(figsize=(figsize1, figsize2))

plt.plot(c_hist)

#Get peaks from column histogram
from scipy.signal import find_peaks_cwt


for i in range(len(c_hist)):
    if (i < 100  or c_hist[i] < c_thredhold):
        c_hist[i] = 0
    
print(c_hist)    
        
# This finds all the peaks in the distribution. Actually works really really well.
peaks = find_peaks_cwt(c_hist, np.arange(12, 300))
peaks = peaks[np.where(peaks > 200)]
peaks = peaks[np.where(peaks < 2100)]

print(peaks)


plt.figure(figsize=(30, 30))
plt.imshow(im > 25, cmap = "gray")
plt.axhline(y=start, color = "r")
plt.axhline(y=end, color = "r")

for peak in peaks:
    plt.axvline(x=peak)
    
plt.show()











































