from os import listdir
from skimage import io
from tqdm import trange

directory = "pages/"

save_directory = "page_data/"

save_name = ""

file_list = listdir(directory)

for i in trange(len(file_list)):
    
    im = io.imread(directory + file_list[i])
    
    if ( i < 100):
        save_name = "00" + str(i + 1) + ".jpg"
    elif (i < 1000):
        save_name = "0" + str(i + 1) + ".jpg"
    else:
        save_name = str(i + 1) + ".jpg"
        
    io.imsave(save_directory + save_name, im)