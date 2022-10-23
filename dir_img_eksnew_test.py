'''
Author: eksnew
Description: 
Date: 2022-10-21 14:14:45
LastEditTime: 2022-10-22 21:35:39
LastEditors: eksnew
'''
import base64
import skimage.io
import cv2 as cv

import base64
import matplotlib.pyplot as plt  # plt 用于显示图片

import cv2
import numpy as np
from mmdet.apis import init_detector, inference_detector, async_inference_detector
# import store

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


def base64_to_img(base64_str):
    # 传入为RGB格式下的base64，传出为RGB格式的numpy矩阵
    byte_data = base64.b64decode(base64_str)  #将base64转换为二进制
    encode_image = np.asarray(bytearray(byte_data),
                              dtype="uint8")  # 二进制转换为一维数组
    img_array = cv2.imdecode(encode_image, cv2.IMREAD_COLOR)  # 用cv2解码为三通道矩阵
    # img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)  # BGR2RGB
    return img_array


def main():
    # print("hello python!")
    # 测试样图
    # base64img = 'iVBORw0KGgoAAAANSUhEUgAAAH0AAAB9AQAAAACn+1GIAAAByklEQVR4Xr2VMY7lIAyGjSjokgsgcQ13XCm5wCS5QHIlOq6BlAvkdRQIr+HN6O1WZpuJUqBPCrZ//3aA/n0y/A6oAHOmK967oR30EPB0GlexALqL7iGA+gRYQ5oMnTAMkHZv53D/B/CgAqzxc4cAOFMsG9k1f1IXAMCE99nfH4EE0KWmI9jJu676AMgFTFq5Mg8LuBFQ0T1eV0xb1kdseYiAsjsNq84luiv0sBKo3i6YVrqPmFToAsmgqFBWYu3dboYAxbRFu+X7yPrxQ6BCmaPmr48WuVtbBIYqsh3cg/rI7Q4RUKQd9RXTYuALm4QyILsRAJeYy9bCyqAC7caqfL8oqdiLEwFShbR4vuk7dRGwhKqZjR3EEjZLySDcFe2E9Hir4hDg3rLqFxUV+TAGIK1RExXgO8IQoMjGsVsoCzZVxgDwcQ6O53vu0yACdpCiNtPVO/bdCCCCLw7Lw8o+ao2SQTXuyuwgxxsR+pYSATeJfbqxu1HXPkAiaFsK0kygsj5NT10EvAu9e5GdDDd5DPAohLZyFp/eqQ+BNhB2Jv2Y1uwRcBp6sfCG832HlYCnizSr2OUfA+1P6B5gU+gH3xIKoO31v55fAn8AgnuZPZMcP7cAAAAASUVORK5CYII='
    # 解码
    # imgdata = base64.b64decode(base64img)
    # 进行一个魔法
    # base642Mat = lambda base64code: cv2.imdecode(
    #     np.frombuffer(base64.decode(base64code)), True)

    # real_pic = base642Mat(base64img)
    # real_pic = skimage.io.imread(imgdata, plugin='imageio')
    # print(real_pic)

    real_pic = base64_to_img(base64img)
    # print(real_pic.shape)
    # print(type(real_pic.shape))
    # cv.imshow("Login", real_pic)
    # cv.waitKey()

    config_file_rcnn = 'X:/Codes/2022/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    checkpoint_file_rcnn = 'X:/Codes/2022/mmdetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    device = 'cuda:0'

    model_rcnn = init_detector(config_file_rcnn,
                               checkpoint_file_rcnn,
                               device=device)

    result_rcnn = inference_detector(model_rcnn, real_pic)
    print(get_info_from_model_result(result_rcnn, real_pic.shape, 0.6))
    # print(model_rcnn)
    # img = model_rcnn.show_result(real_pic,
    #                              result_rcnn,
    #                              bbox_color=(0, 255, 0),
    #                              text_color=(0, 255, 0))

    # cv.imshow("Login", img)
    # cv.waitKey()


if __name__ == "__main__":
    main()