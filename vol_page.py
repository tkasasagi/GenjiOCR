from os import listdir
import pandas as pd
from tqdm import trange
from skimage import io

textdata = pd.read_csv("text_data.csv", header = None)

page = [55, 101, 24, 103, 104, 67, 60, 22, 98, 108, 10, 93, 86, 69, 47, 11, 
        38,  44, 63, 43,  102, 84, 29, 44, 40, 45,  8,  36, 56, 29, 78, 38, 
        49, 204, 206, 80, 38, 29, 144, 39, 44, 27, 26, 83, 79, 76, 180, 40, 
        193, 134, 144, 113, 134, 36]
sum(page)

directory = "pages/"

save_directory = "realpages/"

filelist = pd.read_csv("filelist.csv")

count = 0
'''
filelist["filename"].iloc[0:55]
filelist["filename"].iloc[0 + 55: 55 + 101]
filelist["filename"].iloc[0 + 55 + 101: 101 + 24]
'''

x = 0
y = 55
for i in range(len(page)):
    print("first location = " , x)
    print("second location = " , x + page[i])
    filename = filelist["filename"].iloc[x: x + page[i]]
    print(filename)
    for j in range(len(filename)):
        #open file
        print(filename[j])
        #im = io.imread(directory + filename[j])
        
        #save file
        #io.imsave(save_directory + str(i + 1) + "_" + str(j + 1) + ".jpg", im)

    x = x + page[i]
    print(x)
