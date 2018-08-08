from os import listdir
from skimage import io
from skimage.filters import threshold_sauvola
from skimage.color import rgb2gray
from skimage import img_as_uint

#Get file list in the whole directory

directory = "genjidata/image/"

file_list = listdir(directory)

#Read one image

img = io.imread("dataset/" + file_list[167])

#Change image to grayscale

image = rgb2gray(img)

#Sauvola parameter

window_size = 39
k = 0.3

#Sauvola binarization

thresh_sauvola = threshold_sauvola(image, window_size=window_size, k = k)

binary_sauvola = image > thresh_sauvola

#Change boolean matrix to uint

biimg = img_as_uint(binary_sauvola)

#Save file

io.imsave(file_list[167], biimg)

#visualization

import matplotlib.pyplot as plt

plt.figure(figsize=(40, 30))

plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.axis('off')

plt.show()

