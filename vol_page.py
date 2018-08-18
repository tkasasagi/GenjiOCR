from os import listdir
import pandas as pd
from tqdm import trange
from skimage import io

textdata = pd.read_csv("text_data.csv", header = None)


page = [55, 101, 24, 103, 104, 67, 60, 22, 98, 108, 10, 93, 86, 69, 47, 11, 
        38,  44, 63, 43,  102, 84, 29, 44, 40, 45,  8,  36, 56, 29, 78, 38, 
        49, 204, 206, 80, 38, 29, 144, 39, 44, 27, 26, 83, 79, 76, 180, 40, 
        193, 134, 144, 113, 134, 36]




directory = "pages/"

save_directory = "realpages/"

filelist = pd.read_csv("filelist.csv")

count = 0

x = 0
y = 0
pagecount = 1
for j in trange(len(page)):
    #x = 55
    y = y + page[j]
    
    filename = filelist["filename"].iloc[x: y]
    
    #print(filename)
    pagecount = 1
    for i in range(x, y):
        im = io.imread(directory + filename[i])
        
        io.imsave(save_directory + str(j + 1) + "_" + str(pagecount) + ".jpg", im)
        pagecount = pagecount + 1
    x = x + page[j]








