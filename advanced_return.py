'''
Author: eksnew
Description: advanced_return.py 是为优化服务端返回内容而编写的Python文件。
Date: 2022-10-21 21:49:48
LastEditTime: 2022-10-21 23:17:28
LastEditors: eksnew
'''

import numpy as np

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


def get_info_from_model_result(model_result: list,
                               threshold: float = 0.3) -> dict:
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