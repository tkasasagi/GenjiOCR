from os import listdir
from skimage import io
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

directory = "realpages/"

save_directory = "columns/"

#Read filename
filename = "1_17.jpg"

r_thredhold = 0.03
c_thredhold = 0.1

extend_h_border = 80
extend_v_border = 5

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

start = index[0][0]  - extend_v_border
end   = index[0][-1] + extend_v_border

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


#This just shows all the peaks
print(peaks)

plt.figure(figsize=(15, 15))
plt.imshow(im > 25, cmap = "gray")
plt.axhline(y=start, color = "r")
plt.axhline(y=end, color = "r")

for peak in peaks:
    plt.axvline(x=peak)
    
plt.show()

#save here. Iterate by number of peaks
count = len(peaks) - 1
for j in range(len(peaks)):
    #cut column
    peak = peaks[count]
    crop_column = im[start:end, peak - extend_h_border: peak + extend_h_border]
    if (np.sum(crop_column) < 95200000):
        #plt.figure(figsize=(20, 20))
        #plt.imshow(crop_column, cmap='gray')
        save_name = filename[:-4] + "_" + str(j + 1) + ".jpg"
        #print(save_name)
        io.imsave(save_directory + save_name, crop_column)
    count -=1








































