# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 02:30:41 2019

@author: yyw
"""

import numpy as np
import skimage.io
import skimage.restoration
import skimage.exposure
path= 'C:/Users/yyw/Downloads/taobao/a/TB24c7ls_lYBeNjSszcXXbwhFXa_!!2871484755.jpg'
img = skimage.io.imread(path)
msk = skimage.io.imread('/Users/fred/desktop/mask.png')
msk = skimage.exposure.rescale_intensity(msk, in_range='image', out_range=(0,1))
newimg = skimage.restoration.inpaint_biharmonic(img, msk, multichannel=True)
skimage.io.imsave('/Users/fred/desktop/kitty_inpaint_biharmonic.png', newimg)