"""
Author: eksnew
Description:
Date: 2022-10-20 15:13:58
LastEditTime: 2022-10-21 15:02:57
LastEditors: eksnew
"""
import base64

import cv2
import numpy as np
import store
from mmdet.apis import inference_detector
from rest_framework.response import Response
from rest_framework.views import APIView

# from advanced_return import get_info_from_model_result

# Create your views here.

# 一个继承APIView的后端接口
class CodeView(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data)# 接收请求体传过来的数据
        print(request.data['type'])
        if request.data['type'] == "camera":
            pic_base64 = request.data[
                'base1']  # print("pic_base64:", type(pic_base64) ) #  <class 'str'>
            pic = base64.b64decode(
                pic_base64
            )  # base64解码为 \x**\x**\x**\x** #print("pic:", type(pic)) # pic: <class 'bytes'>

            # 改为不保存在本地，直接传递
            real_pic = store.base64_to_img(pic_base64)
            score = float(request.data['score_thr'])
            print('score_thr', score)
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
            elif request.data['methodChoice'] == 3:
                result_method = inference_detector(
                    store.model_transfer,
                    real_pic)

            obj_dic = store.get_info_from_model_result(result_method, real_pic.shape, score)
            print(type(obj_dic))
            print(obj_dic)
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

