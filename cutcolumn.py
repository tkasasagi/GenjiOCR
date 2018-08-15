from os import listdir
from skimage import io
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

directory = "page_data/"

save_directory = "column/"

filename = "001.jpg"

#Open image file

im = io.imread(directory + filename)

v_hist = (im < 25).mean(axis=1)

plt.figure(figsize=(30, 20))
plt.plot(v_hist)

"""
#get histogram for start 
for i in range(im.shape[0]):
    if (im[0][i])
    print(sum(im[i]))
    """