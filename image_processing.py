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

    
import matplotlib
import matplotlib.pyplot as plt

from skimage import io

from skimage.data import page
from skimage.filters import threshold_sauvola

thresh_sauvola = threshold_sauvola(image, window_size=15, k = 0.3)

binary_sauvola = image > thresh_sauvola


plt.subplot(2, 2, 4)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()