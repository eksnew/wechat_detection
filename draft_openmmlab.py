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

import cv2
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
import numpy as np
from mmdet.apis import init_detector, inference_detector

# from advanced_return import get_info_from_model_result

type_list = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train',
    'truck', 'boat', 'traffic_light', 'fire_hydrant', 'stop_sign',
    'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag',
    'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports_ball', 'kite',
    'baseball_bat', 'baseball_glove', 'skateboard', 'surfboard',
    'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork', 'knife', 'spoon',
    'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
    'hot_dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted_plant',
    'bed', 'dining_table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
    'keyboard', 'cell_phone', 'microwave', 'oven', 'toaster', 'sink',
    'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy_bear',
    'hair_drier', 'toothbrush'
]
PALETTE = [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230),
           (106, 0, 228), (0, 60, 100), (0, 80, 100), (0, 0, 70),
           (0, 0, 192), (250, 170, 30), (100, 170, 30), (220, 220, 0),
           (175, 116, 175), (250, 0, 30), (165, 42, 42), (255, 77, 255),
           (0, 226, 252), (182, 182, 255), (0, 82, 0), (120, 166, 157),
           (110, 76, 0), (174, 57, 255), (199, 100, 0), (72, 0, 118),
           (255, 179, 240), (0, 125, 92), (209, 0, 151), (188, 208, 182),
           (0, 220, 176), (255, 99, 164), (92, 0, 73), (133, 129, 255),
           (78, 180, 255), (0, 228, 0), (174, 255, 243), (45, 89, 255),
           (134, 134, 103), (145, 148, 174), (255, 208, 186),
           (197, 226, 255), (171, 134, 1), (109, 63, 54), (207, 138, 255),
           (151, 0, 95), (9, 80, 61), (84, 105, 51), (74, 65, 105),
           (166, 196, 102), (208, 195, 210), (255, 109, 65), (0, 143, 149),
           (179, 0, 194), (209, 99, 106), (5, 121, 0), (227, 255, 205),
           (147, 186, 208), (153, 69, 1), (3, 95, 161), (163, 255, 0),
           (119, 0, 170), (0, 182, 199), (0, 165, 120), (183, 130, 88),
           (95, 32, 0), (130, 114, 135), (110, 129, 133), (166, 74, 118),
           (219, 142, 185), (79, 210, 114), (178, 90, 62), (65, 70, 15),
           (127, 167, 115), (59, 105, 106), (142, 108, 45), (196, 172, 0),
           (95, 54, 80), (128, 76, 255), (201, 57, 1), (246, 0, 122),
           (191, 162, 208)]


def get_info_from_model_result(model_result: list, threshold: float = 0.3) -> dict:
    '''
    get_info_from_model_result 函数被设计用于返回检测到的类型、矩形坐标及置信度list。
        @param model_result: list inference_detector返回的结果
        @param threshold: float 置信度阈值
    '''
    obj_dic = {}
    for i, class_info in enumerate(model_result):
        if class_info.shape[0]:
            # print(class_info.shape, class_info, type_list[i])
            for j, obj_info in enumerate(class_info):
                if obj_info[-1] <= threshold:
                    continue
                obj_dic[type_list[i] + str(j + 1)] = np.insert(obj_info, 0, i)
                # print(np.insert(obj_info, 0, i))

    return obj_dic


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
# print(result)
#  model.show_result(img, result)

# 获取信息
obj_dic = get_info_from_model_result(result_rcnn, 0.3)
print(obj_dic)

# 将推理的结果保存
img = model_rcnn.show_result(img,
                             result_rcnn,
                             bbox_color=(0, 255, 0),
                             text_color=(0, 255, 0))

for key, value in obj_dic.items():
    # print(value, value[0], type(value[0]))
    cv2.circle(img, (int(value[1]), int(value[2])), 10, PALETTE[int(value[0])], -1)
img = cv2.resize(img, None, fx=0.45, fy=0.45)
cv2.imshow('res', img)
cv2.waitKey(0)

# img = model_detectors.show_result(img, result_detectors, bbox_color=(255, 0, 0), text_color=(255, 0, 0))
# img = model_yolo.show_result(img, result_yolo, bbox_color=(0, 0, 255), text_color=(0, 0, 255))
# cv2.imwrite(r'C:\Users\eksnew\OneDrive\Desktop\DRAFT\result3.jpg', img)
# cv2.imwrite(r'X:\Codes\2022\wechat_detection\result_test3.jpg', img)
# model.show_result(img, result, out_file='D:/DIP/result.jpg')
# print("Result Saved.")
