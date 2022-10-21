
from mmdet.apis import init_detector, inference_detector
import cv2
global config_file_rcnn
config_file_rcnn = 'detection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
global config_file_detectors
config_file_detectors = 'detection/configs/detectors/detectors_cascade_rcnn_r50_1x_coco.py'
global config_file_yolo
config_file_yolo = 'detection/configs/yolo/yolov3_d53_320_273e_coco.py'


global checkpoint_file_rcnn
checkpoint_file_rcnn = 'detection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
global checkpoint_file_detectors
checkpoint_file_detectors = 'detection/checkpoints/detectors_cascade_rcnn_r50_1x_coco-7b6ec977.pth'
global checkpoint_file_yolo
checkpoint_file_yolo = 'detection/checkpoints/yolov3_d53_320_273e_coco-421362b6.pth'


global device
device = 'cuda:0'

global model_rcnn
global model_detectors
global model_yolo



# model_rcnn = init_detector(config_file_rcnn, checkpoint_file_rcnn, device=device)
