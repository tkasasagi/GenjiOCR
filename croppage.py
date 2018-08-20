from tqdm import trange
import numpy as np
from skimage.data import imread
import matplotlib.pyplot as plt
from skimage import io
#Get all file list
from os import listdir

directory = "realpages/"

file_list = listdir(directory)

save_directory = "croppages/"

#Loop all files

for i in trange(len(file_list)):
#for i in range(0, 10):
    #Read data
    image_file = directory + file_list[i]
    im = imread(image_file)
    #plt.figure(figsize=(30, 20))
    #plt.imshow(im, cmap='gray')
    #Get shape
    
    shape = im.shape
    #print(shape)
    
    crop_im = im[17:shape[0], 10:shape[1] - 17]
    
    #plt.figure(figsize=(30, 20))
    #plt.imshow(crop_im, cmap='gray')
        
    #Save
    
    save_name = file_list[i]
    #print(save_name)
    io.imsave(save_directory + save_name, crop_im)








