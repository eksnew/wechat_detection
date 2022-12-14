'''
Author: eksnew
Description: 
Date: 2022-10-03 23:25:23
LastEditTime: 2022-10-19 19:35:49
LastEditors: eksnew
'''
# '''
# Author: eksnew
# Description:
# Date: 2022-04-22 15:57:34
# LastEditTime: 2022-09-19 13:27:35
# LastEditors: eksnew
# '''
# from mmdet.apis import init_detector, inference_detector

# config_file = 'X:/Codes/2022/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
# # 从 model zoo 下载 checkpoint 并放在 `checkpoints/` 文件下
# # 网址为: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
# checkpoint_file = 'X:/Codes/2022/mmdetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
# device = 'cuda:0'
# # 初始化检测器
# model = init_detector(config_file, checkpoint_file, device=device)
# # 推理演示图像
# inference_detector(model, 'X:/Codes/2022/mmdetection/demo/demo.jpg')
# img = model_rcnn.show_result(img,
#                              result_rcnn,
#                              bbox_color=(0, 255, 0),
#                              text_color=(0, 255, 0))
# img = model_detectors.show_result(img,
#                                   result_detectors,
#                                   bbox_color=(255, 0, 0),
#                                   text_color=(255, 0, 0))
# img = model_yolo.show_result(img,
#                              result_yolo,
#                              bbox_color=(0, 0, 255),
#                              text_color=(0, 0, 255))
# cv2.imwrite(r'C:\Users\eksnew\OneDrive\Desktop\DRAFT\result3.jpg', img)
# #model.show_result(img, result, out_file='D:/DIP/result.jpg')
# print("Result Saved.")
from mmdet.apis import init_detector, inference_detector
import cv2

config_file_rcnn = 'X:/Codes/2022/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
# config_file_detectors = 'configs/detectors/detectors_cascade_rcnn_r50_1x_coco.py'
# config_file_yolo = 'configs/yolo/yolov3_d53_320_273e_coco.py'
# 从 model zoo 下载 checkpoint 并放在 `checkpoints/` 文件下
# 网址为: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
checkpoint_file_rcnn = 'X:/Codes/2022/mmdetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
# checkpoint_file_detectors = 'checkpoints/detectors_cascade_rcnn_r50_1x_coco-7b6ec977.pth'
# checkpoint_file_yolo = 'checkpoints/yolov3_d53_320_273e_coco-421362b6.pth'

device = 'cuda:0'
# 初始化检测器
model_rcnn = init_detector(config_file_rcnn,
                           checkpoint_file_rcnn,
                           device=device)
# model_detectors = init_detector(config_file_detectors, checkpoint_file_detectors, device=device)
# model_yolo = init_detector(config_file_yolo, checkpoint_file_yolo, device=device)
# 推理演示图像
# img = 'X:/Codes/2022/mmdetection/demo/demo.jpg'
# img = r'X:\Codes\2022\wechat_detection\test1.jpg'
# img = r'X:\Codes\2022\wechat_detection\test2.jpg'
img = r'X:\Codes\2022\wechat_detection\test3.jpg'
result_rcnn = inference_detector(model_rcnn, img)
# result_detectors = inference_detector(model_detectors, img)
# result_yolo = inference_detector(model_yolo, img)
#print(result)
#  model.show_result(img, result)
# 将推理的结果保存
img = model_rcnn.show_result(img,
                             result_rcnn,
                             bbox_color=(0, 255, 0),
                             text_color=(0, 255, 0))
# img = model_detectors.show_result(img, result_detectors, bbox_color=(255, 0, 0), text_color=(255, 0, 0))
# img = model_yolo.show_result(img, result_yolo, bbox_color=(0, 0, 255), text_color=(0, 0, 255))
# cv2.imwrite(r'C:\Users\eksnew\OneDrive\Desktop\DRAFT\result3.jpg', img)
cv2.imwrite(r'X:\Codes\2022\wechat_detection\result_test3.jpg', img)
#model.show_result(img, result, out_file='D:/DIP/result.jpg')
print("Result Saved.")