from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import base64
import matplotlib.pyplot as plt # plt 用于显示图片

import cv2
import numpy as np
from mmdet.apis import init_detector, inference_detector, async_inference_detector

import store
# Create your views here.

# 一个继承APIView的后端接口
class CodeView(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data)# 接收请求体传过来的数据
        # print(request.data['type'])
        if request.data['type'] == "camera":
            pic_base64 = request.data['base1']
            #print("pic_base64:", type(pic_base64) ) #  <class 'str'>
            pic = base64.b64decode(pic_base64)  # base64解码为 \x**\x**\x**\x**
            #print("pic:", type(pic)) # pic: <class 'bytes'>

            # nparr = np.fromstring(pic, np.uint8)
            # pic_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # <class 'numpy.ndarray'># 函数从指定的内存缓存中读取数据，并把数据转换(解码)成图像格式;主要用于从网络传输数据中恢复出图像。
            # print("Pic_np Get.")
            # 通过opencv显示图片
            #resize_img = cv2.resize(pic_np, dsize=(300, 300))
            #cv2.imshow("img", resize_img)
            #cv2.waitKey(1000)
            #cv2.destroyAllWindows()
            # base64转图片保存到本地
            f = open('demo.jpg', 'wb')
            f.write(pic)
            f.close()
            #print("Image Saved.")
            # 调用模型检测识别
            # result_rcnn = async_inference_detector(store.model_rcnn, pic_np)#'demo.jpg')
            result_rcnn = inference_detector(store.model_rcnn, 'demo.jpg')
            #print(type(result_rcnn)) # <class 'list'>
            # img = store.model_rcnn.show_result(pic_np, result_rcnn, bbox_color=(0, 255, 0), text_color=(0, 255, 0))
            img = store.model_rcnn.show_result('demo.jpg', result_rcnn, bbox_color=(0, 255, 0), text_color=(0, 255, 0))
            #print("result_img:", type(img) )  # result_img: <class 'numpy.ndarray'>
            retval, img_buffer = cv2.imencode('.jpg', img)
            img_str = base64.b64encode(img_buffer)
            result_base64 = img_str
            # print('result_base64:', result_base64)
            #cv2.imwrite('result1_888.jpg', img)
            print("Result Saved66.")

        print("POST结束 return------------------------------------------------------------------")
        return Response({"state": True, "result_base64": result_base64})# 返回值一个字典


