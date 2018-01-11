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

labels=measure.label(img5,connectivity=2)  #连通区域标记
print('coin number:',labels.max())  #显示连通区域块数(从0开始标记)
plt.imshow(img5)
i = 0
for region in measure.regionprops(labels): #循环得到每一个连通区域属性集
    
    #忽略小区域
    if region.area < 10:
        continue

    #绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    #rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='yellow', linewidth=2)
    #ax1.add_patch(rect)
    plt.text((minc + maxc)/2-10,(minr + maxr)/2, region.area,color='red' )
    #print("The area of number ",i ," coin is ", region.area)
    i = i+1

 
plt.show()



