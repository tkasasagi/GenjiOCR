from tqdm import tqdm
import numpy as np
from skimage.data import imread
import matplotlib.pyplot as plt

#Get all file list
from os import listdir

directory = "binarization/"

file_list = listdir(directory)
edit_list = []
threshold = 0.35

for i in tqdm(range(len(file_list))):

    image_file = directory + file_list[i]
    im = imread(image_file)
    
    #Get shape
    
    shape = im.shape
    #print(shape)
    
    
    #print(im)
    
    #plt.figure(figsize=(30, 20))
    #plt.imshow(im, cmap='gray')

    
    #Get peak histogram
    
    v_hist = (im < 25).mean(axis=0)
    
    #plt.figure(figsize=(30, 20))
    #plt.plot(v_hist)
    
    index = np.where(v_hist == (np.max(v_hist)))
    #if (np.max(v_hist) < threshold) or (index[0][0] < 2000):
    if (np.max(v_hist) < threshold):
        edit_list.append(file_list[i])
    #print(type(index[0]))
    

    
import pandas as pd

editlist = pd.DataFrame()
editlist['list'] = edit_list
editlist.to_csv("editlist.csv", index = False)