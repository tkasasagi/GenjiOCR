from tqdm import tqdm
import numpy as np
from skimage.data import imread
import matplotlib.pyplot as plt

#Get all file list
from os import listdir

directory = "binarization/"


image_file = directory + "200003803_00896.jpg"
im = imread(image_file)

#Get shape

shape = im.shape
#print(shape)


#print(im)

plt.figure(figsize=(30, 20))
plt.imshow(im, cmap='gray')




#Get peak histogram

v_hist = (im < 25).mean(axis=0)

plt.figure(figsize=(30, 20))
plt.plot(v_hist)

index = np.where(v_hist == (np.max(v_hist)))
print(index[0][0])
#print(type(index[0]))