from os import listdir
from skimage import io
from skimage.filters import threshold_sauvola, threshold_otsu
from skimage.color import rgb2gray
from skimage import img_as_uint

#Get file name

directory = "fix/"

save_directory = "pages/"

file_name = "200003803_01474_0.jpg"

#Read one image

img = io.imread(directory + file_name)

img.shape

#Change image to grayscale

image = rgb2gray(img)

#Sauvola parameter

window_size = 35
k = 0.3

#Sauvola binarization

thresh_sauvola = threshold_sauvola(image, window_size=window_size, k = k)
#thresh_sauvola = threshold_otsu(image)

binary_sauvola = image > thresh_sauvola

#Change boolean matrix to uint

biimg = img_as_uint(binary_sauvola)

#Save file

io.imsave(save_directory + file_name, biimg)

#visualization
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(30, 20))

plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.axis('off')

plt.show()

#Get peak histogram
    
#v_hist = (binary_sauvola < 25).mean(axis=0)

v_hist = (binary_sauvola < 25)

plt.figure(figsize=(30, 20))
plt.plot(v_hist)
'''





































