'''
Author: eksnew
Description: 
Date: 2022-10-20 15:13:58
LastEditTime: 2022-10-21 15:02:57
LastEditors: eksnew
'''
import base64

import cv2
import numpy as np
import store
from mmdet.apis import inference_detector
from rest_framework.response import Response
from rest_framework.views import APIView

# from advanced_return import get_info_from_model_result

# Create your views here.

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


# 一个继承APIView的后端接口
class CodeView(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data)# 接收请求体传过来的数据
        # print(request.data['type'])
        if request.data['type'] == "camera":
            pic_base64 = request.data[
                'base1']  # print("pic_base64:", type(pic_base64) ) #  <class 'str'>
            pic = base64.b64decode(
                pic_base64
            )  # base64解码为 \x**\x**\x**\x** #print("pic:", type(pic)) # pic: <class 'bytes'>

            # 改为不保存在本地，直接传递
            real_pic = base64_to_img(pic_base64)

            # 调用模型检测识别
            if request.data['methodChoice'] == 0:  # faster_rcnn
                result_method = inference_detector(
                    store.model_rcnn,
                    real_pic)
            elif request.data['methodChoice'] == 1:
                result_method = inference_detector(
                    store.model_detectors,
                    real_pic)
            elif request.data['methodChoice'] == 2:  # 2：yolo
                result_method = inference_detector(
                    store.model_yolo,
                    real_pic)
            obj_dic = get_info_from_model_result(result_method, 0.3)
            return Response({
                    "state": 1,
                    "result_base64": obj_dic
                })  # 返回值一个字典

                # 通过opencv显示图片
                # resize_img = cv2.resize(pic_np, dsize=(300, 300))
                # cv2.imshow("img", resize_img)
                # cv2.waitKey(1000)
                # cv2.destroyAllWindows()

                # # base64转图片保存到本地
                # f = open('demo.jpg', 'wb')
                # f.write(pic)
                # f.close()
        #     if request.data['methodChoice'] == 0:  # faster_rcnn
        #         result_rcnn = inference_detector(
        #             store.model_rcnn,
        #             real_pic)  #print(type(result_rcnn)) # <class 'list'>
        #         img = store.model_rcnn.show_result(
        #             real_pic,
        #             result_rcnn,
        #             bbox_color=(0, 255, 0),
        #             text_color=(0, 255, 0)
        #         )  #print("result_img:", type(img) )  # result_img: <class 'numpy.ndarray'>
        #         print("rcnn----------.")
        #     elif request.data['methodChoice'] == 1:  # detectors_rcnn
        #         result_detectors = inference_detector(
        #             store.model_detectors,
        #             real_pic)  #print(type(result_rcnn)) # <class 'list'>
        #         img = store.model_detectors.show_result(
        #             real_pic,
        #             result_detectors,
        #             bbox_color=(255, 0, 0),
        #             text_color=(255, 0, 0)
        #         )  #print("result_img:", type(img) )  # result_img: <class 'numpy.ndarray'>
        #         print("detectors----------.")
        #     elif request.data['methodChoice'] == 2:  # 2：yolo
        #         result_yolo = inference_detector(
        #             store.model_yolo,
        #             real_pic)  #print(type(result_rcnn)) # <class 'list'>
        #         img = store.model_yolo.show_result(
        #             real_pic,
        #             result_yolo,
        #             bbox_color=(0, 0, 255),
        #             text_color=(0, 0, 255)
        #         )  #print("result_img:", type(img) )  # result_img: <class 'numpy.ndarray'>
        #         print("yolo----------.")
        #     retval, img_buffer = cv2.imencode('.jpg', img)
        #     img_str = base64.b64encode(img_buffer)
        #     result_base64 = img_str
        #     #cv2.imwrite('result1_888.jpg', img)
        #     print("Result Saved66.")
        # print(
        #     "POST结束 return------------------------------------------------------------------"
        # )

