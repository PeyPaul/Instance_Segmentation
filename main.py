### Import modules

import pixellib
from pixellib.instance import  instance_segmentation
import cv2

### Setup model

segmentation_model = instance_segmentation()
segmentation_model.load_model('mask_rcnn_coco.h5')

### Real Time Capture

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    cv2.imshow('Instance Segmentation', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()