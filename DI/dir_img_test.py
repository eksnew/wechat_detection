'''
Author: eksnew
Description: 
Date: 2022-10-21 14:14:45
LastEditTime: 2022-10-21 15:01:34
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

    cv.imshow("Login", real_pic)
    cv.waitKey()

    config_file_rcnn = 'X:/Codes/2022/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    checkpoint_file_rcnn = 'X:/Codes/2022/mmdetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    device = 'cuda:0'

    model_rcnn = init_detector(config_file_rcnn,
                               checkpoint_file_rcnn,
                               device=device)

    result_rcnn = inference_detector(model_rcnn, real_pic)
    img = model_rcnn.show_result(real_pic,
                                 result_rcnn,
                                 bbox_color=(0, 255, 0),
                                 text_color=(0, 255, 0))

    cv.imshow("Login", img)
    cv.waitKey()


if __name__ == "__main__":
    main()