#This code is to cut half page and save them into correct file name
from tqdm import tqdm
import numpy as np
from skimage.data import imread
import matplotlib.pyplot as plt

#Get all file list
from os import listdir

directory = "binarization5/"

file_list = listdir(directory)

save_directory = "pages/"

#Loop all files

for i in tqdm(range(len(file_list))):
    #Read data
    image_file = directory + file_list[i]
    im = imread(image_file)
    
    #Get shape
    
    shape = im.shape
    #print(shape)
    
    #print(im)
    '''
    plt.figure(figsize=(30, 20))
    plt.imshow(im, cmap='gray')
    '''
    
    
    
    #Get peak histogram
    
    v_hist = (im < 25).mean(axis=0)
    '''
    plt.figure(figsize=(30, 20))
    plt.plot(v_hist)
    '''
    index = np.where(v_hist == (np.max(v_hist)))
    #print(index[0][0])
    #print(type(index[0]))
    
    #Crop Right
    
    crop_im_right = im[0:shape[0], int(index[0][0]):shape[1]]
    '''
    plt.figure(figsize=(30, 20))
    plt.imshow(crop_im_right, cmap='gray')
    '''
    #Crop Left
    
    crop_im_left  = im[0:shape[1], 0:int(index[0][0])]
    '''
    plt.figure(figsize=(30, 20))
    plt.imshow(crop_im_left, cmap='gray')
    '''
    #Save
    from skimage import io
    save_name = file_list[i][:-4]
    print(save_name)
    io.imsave(save_directory + save_name + "_0.jpg", crop_im_right)
    io.imsave(save_directory + save_name + "_1.jpg", crop_im_left)






















  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
