'''
Author: eksnew
Description: 
Date: 2022-10-20 15:13:58
LastEditTime: 2022-10-22 15:31:43
LastEditors: eksnew
'''
from mmdet.apis import init_detector, inference_detector
import cv2
import numpy as np
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

# 类型列表
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
palette_list = [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230),
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
                (166, 196, 102), (208, 195, 210), (255, 109, 65),
                (0, 143, 149), (179, 0, 194), (209, 99, 106), (5, 121, 0),
                (227, 255, 205), (147, 186, 208), (153, 69, 1), (3, 95, 161),
                (163, 255, 0), (119, 0, 170), (0, 182, 199), (0, 165, 120),
                (183, 130, 88), (95, 32, 0), (130, 114, 135), (110, 129, 133),
                (166, 74, 118), (219, 142, 185), (79, 210, 114), (178, 90, 62),
                (65, 70, 15), (127, 167, 115), (59, 105, 106), (142, 108, 45),
                (196, 172, 0), (95, 54, 80), (128, 76, 255), (201, 57, 1),
                (246, 0, 122), (191, 162, 208)]

global get_info_from_model_result


def get_info_from_model_result(model_result: list,
                               img_shape: tuple,
                               threshold: float = 0.3) -> dict:
    '''
    get_info_from_model_result 函数被设计用于返回检测到的类型、矩形坐标及置信度list。
        @param model_result: list inference_detector返回的结果
        @param threshold: float 置信度阈值
    '''
    obj_dic = {}
    for i, class_info in enumerate(model_result):
        # 若有检测结果
        if class_info.shape[0]:
            # print(class_info.shape, class_info, type_list[i])
            for j, obj_info in enumerate(class_info):
                # 置信度筛选
                if obj_info[-1] <= threshold:
                    continue
                # 改传比例
                # for loc in range(0, 4, 2):
                #     pass
                # for loc in range(1, 4, 2):
                #     pass
                obj_info[0] = obj_info[0] / img_shape[0]
                obj_info[1] = obj_info[1] / img_shape[1]
                obj_info[2] = obj_info[2] / img_shape[0]
                obj_info[3] = obj_info[3] / img_shape[1]
                # 在首元素添加序号
                obj_dic[type_list[i] + str(j + 1)] = np.insert(obj_info, 0, i)
                # print(np.insert(obj_info, 0, i))

    return obj_dic


global base64_to_img


def base64_to_img(base64_str):
    """
    base64转img函数。传入RGB格式下的base64，传出为RGB格式的numpy矩阵。
    """
    byte_data = base64.b64decode(base64_str)  # 将base64转换为二进制
    encode_image = np.asarray(bytearray(byte_data),
                              dtype="uint8")  # 二进制转换为一维数组
    img_array = cv2.imdecode(encode_image, cv2.IMREAD_COLOR)  # 用cv2解码为三通道矩阵
    # img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)  # BGR2RGB
    return img_array


# model_rcnn = init_detector(config_file_rcnn, checkpoint_file_rcnn, device=device)
