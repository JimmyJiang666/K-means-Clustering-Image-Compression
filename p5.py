import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('Neuschwanstein_small.png')
img = img[:,:,:3] # remove the fourth coordinate alpha
plt.imshow(img)
print(img.shape)