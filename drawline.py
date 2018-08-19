#import
from skimage.data import imread
import matplotlib.pyplot as plt
from skimage.draw import line

#open file
image_file = "dataset2/200003803_00087.jpg"

im = imread(image_file)

im.shape

#draw line

im.line(0, 1000, 1000, 1000)


#save file

