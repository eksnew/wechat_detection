
from mmdet.apis import init_detector, inference_detector
import cv2
global config_file_rcnn
config_file_rcnn = 'detection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

global checkpoint_file_rcnn
checkpoint_file_rcnn = 'detection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

global device
device = 'cuda:0'

global model_rcnn



# model_rcnn = init_detector(config_file_rcnn, checkpoint_file_rcnn, device=device)
