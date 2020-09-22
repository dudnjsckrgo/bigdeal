# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
from ISR.models import RDN

img = Image.open('car1.jpg')
lr_img = np.array(img)

rdn = RDN(arch_params={'C':6, 'D':20, 'G':64, 'G0':64, 'x':2})
rdn.model.load_weights('weights/sample_weights/rdn-C6-D20-G64-G064-x2/ArtefactCancelling/rdn-C6-D20-G64-G064-x2_ArtefactCancelling_epoch219.hdf5')

sr_img = rdn.predict(lr_img)
Image.fromarray(sr_img)
cv2.imshow("input image",image)