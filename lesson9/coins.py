import numpy as np
from skimage.data import coins
from skimage import feature ,measure,color
import matplotlib.pyplot as plt
from scipy.ndimage import center_of_mass,filters,morphology,binary_closing,binary_dilation,binary_opening,binary_erosion

img=coins()

edges=feature.canny(img,sigma=3)# canny to take the edge

img1=binary_dilation(edges)
img2=morphology.binary_fill_holes(img1)
img3=binary_erosion(img2)

img5=filters.gaussian_filter(img3,sigma=1)

# center_of_mass()
#plt.imshow(img5)

labels=measure.label(img5,connectivity=2)  #8连通区域标记
print('coin number:',labels.max())  #显示连通区域块数(从0开始标记)

#plt.show()



