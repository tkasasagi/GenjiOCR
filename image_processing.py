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


from skimage import io

#test binarization

img = io.imread("dataset/" + file_list[34])
io.imshow("dataset/" + file_list[34])
io.show()

import matplotlib.pyplot as plt
from skimage.filters import threshold_sauvola

thresh_sauvola = threshold_sauvola(img, window_size=15, k = 0.3)
binary_sauvola = img > thresh_sauvola

binary_sauvola = binary_sauvola * 1

int(binary_sauvola)

io.imsave("test.png", binary_sauvola)





binary_sauvola = img > thresh_sauvola

print(thresh_sauvola)

io.imshow(binary_sauvola)

io.imsave("test.jpg", thresh_sauvola)


plt.subplot(2, 2, 4)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()