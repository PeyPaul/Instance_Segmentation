### Import modules

import pixellib
from pixellib.instance import  instance_segmentation
import cv2

### Setup model

segmentation_model = instance_segmentation()
segmentation_model.load_model('mask_rcnn_coco.h5')