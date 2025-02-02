from os import listdir
from skimage import io
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

directory = "croppages/"

save_directory = "column6/"

#Read filename
filename = listdir(directory)

r_thredhold = 0.03
c_thredhold = 0.05

extend_h_border = 90
extend_v_border = 10

figsize1 = 15
figsize2 = 10

#for iteration in trange(len(filename)):
for iteration in trange(0, 15):
#Open image file

    im = io.imread(directory + filename[iteration])
    #plt.figure(figsize=(30, 28))
    #plt.imshow(im, cmap = 'gray')
    
    v_hist = (im < 25).mean(axis=1)
    
    #plt.figure(figsize=(figsize1, figsize2))
    #plt.plot(v_hist)
    
    #Get location where the block start and end
    #print(filename[iteration])
    index = np.where(v_hist > r_thredhold)
    #print(index[0][0])
    if (index[0][0] > extend_v_border):
        start = index[0][0]  - extend_v_border
    else:
        start = index[0][0]
    if (index[0][-1] + extend_v_border < im.shape[1]):
        end   = index[0][-1] + extend_v_border
    else:
        end = index[0][-1]
    
    #print("start at ", start, " ,end at ", end, " ,total height= ", (end - start))
    #get location of each column
    c_hist = (im < 25).mean(axis=0)
    
    plt.figure(figsize=(figsize1, figsize2))
    
    plt.plot(c_hist)
    
    #Get peaks from column histogram
    from scipy.signal import find_peaks_cwt
    
    
    for i in range(len(c_hist)):
        if (i < 100  or c_hist[i] < c_thredhold):
            c_hist[i] = 0
        
    #print(c_hist)    
            
    # This finds all the peaks in the distribution. Actually works really really well.
    peaks = find_peaks_cwt(c_hist, np.arange(12, 300))
    peaks = peaks[np.where(peaks > 100)]
    peaks = peaks[np.where(peaks < 2100)]
    

    #This just shows all the peaks
    print(peaks)
    
    plt.figure(figsize=(15, 22))
    plt.imshow(im > 25, cmap = "gray")
    plt.axhline(y=start, color = "r")
    plt.axhline(y=end, color = "r")
    
    for peak in peaks:
        plt.axvline(x=peak)
        
    plt.show()
'''
    #save here. Iterate by number of peaks
    count = len(peaks) - 1
    for j in range(len(peaks)):
        #cut column
        peak = peaks[count]
        crop_column = im[start:end, peak - extend_h_border: peak + extend_h_border]
        #plt.figure(figsize=(20, 20))
        #plt.imshow(crop_column, cmap='gray')
        save_name = filename[iteration][:-4] + "_" + str(j + 1) + ".jpg"
        #print(save_name)
        #if (np.sum(crop_column) < 95200000):
        io.imsave(save_directory + save_name, crop_column)
        count -=1
'''







































