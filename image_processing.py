from PIL import Image
from os import listdir

directory = "genjidata/image/"

file_list = listdir(directory)



#Crop and save
dim = (250, 500, 5000, 3550)
for i in range(len(file_list)):
    image = Image.open((directory + file_list[i]))

    crop_img = image.crop(dim)

    crop_img.save("dataset/" + file_list[i])
    
    image.close()


