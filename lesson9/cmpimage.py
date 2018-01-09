from scipy.misc import imread,imsave
import matplotlib.pyplot as plt
import numpy as np
from skimage import data,segmentation,measure,color,feature,morphology
from skimage import io,filters
import matplotlib.patches as mpatches
from PIL import ImageChops
from PIL import Image



im1 = imread("pig3.jpg")
im2 = imread("pig4.jpg")
f1 = im1.astype('float')
f2 = im2.astype('float')

fc1 = np.abs(f1 - f2)
fc1[fc1<50] = 0

img=color.rgb2gray(fc1)
#img=(img<0.5)*1

thresh =filters.threshold_otsu(img) #阈值分割
bw =morphology.closing(img > thresh, morphology.square(3)) #闭运算

cleared = bw.copy()  #复制
#segmentation.clear_border(cleared)  #清除与边界相连的目标物

label_image =measure.label(cleared)  #连通区域标记
borders = np.logical_xor(bw, cleared) #异或
label_image[borders] = -1
#image_label_overlay =color.label2rgb(label_image, img=img) #不同标记用不同颜色显示
print(label_image.max())

fig,(ax0,ax1)= plt.subplots(1,2, figsize=(8, 6))
ax0.imshow(im1)
ax1.imshow(im2)


for region in measure.regionprops(label_image): #循环得到每一个连通区域属性集
    
    #忽略小区域
    if region.area < 20:
        continue

    #绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='yellow', linewidth=2)
    ax1.add_patch(rect)





fig.tight_layout()
plt.show()
