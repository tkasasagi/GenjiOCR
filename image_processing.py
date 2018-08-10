from PIL import Image
from os import listdir
from tqdm import tqdm

directory = "dataset/"

file_list = listdir(directory)



#Crop and save
dim = (100, 100, 4280, 3090)
for i in tqdm(range(len(file_list))):
    image = Image.open((directory + file_list[i]))
    
    #image = Image.open((directory + "200003803_00004.jpg"))
    
    crop_img = image.crop(dim)
    
    #crop_img.show()
    
    crop_img.save("dataset2/" + file_list[i])
    
    image.close()


