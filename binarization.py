from os import listdir

directory = "genjidata/image/"

file_list = listdir(directory)

import matplotlib
import matplotlib.pyplot as plt

from skimage.filters import threshold_sauvola

from skimage import io

matplotlib.rcParams['font.size'] = 9

img = io.imread("dataset/" + file_list[34])

from skimage.color import rgb2gray

image = rgb2gray(img)

window_size = 21
k = 0.3

thresh_sauvola = threshold_sauvola(image, window_size=window_size, k = k)

binary_sauvola = image > thresh_sauvola

plt.figure(figsize=(40, 30))

plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.axis('off')

plt.show()
#plt.savefig("test.png")
from skimage import img_as_float

biimg = img_as_float(binary_sauvola)

io.imsave("test.png", biimg)

from skimage import img_as_uint

biimg = img_as_uint(binary_sauvola)

io.imsave("test.png", biimg)