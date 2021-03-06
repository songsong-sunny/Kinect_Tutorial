# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 11:32
# @Author  : play4fun
# @File    : freenect_cv2_demo1.py
# @Software: PyCharm

"""
freenect_cv2_demo1.py:
http://euanfreeman.co.uk/openkinect-python-and-opencv/

简单例子
"""

import freenect
import cv2
import numpy as np

"""
Grabs a depth map from the  sensor and creates an image from it.
"""

kernel = np.ones((5, 5), np.uint8)


def getDepthMap(mindep=2, maxdep=5):
    depth, timestamp = freenect.sync_get_depth()

    np.clip(depth, a_min=0, a_max=2 ** 10 - 1, out=depth)  # 修剪？
    depth >>= mindep #必须？
    # depth <<= maxdep
    depth = depth.astype(np.uint8)

    return depth


try:
    while True:
        depth4 = getDepthMap(6, 10)
        depth2 = getDepthMap(2, 5)
        # print('depth', type(depth2))

        blur = cv2.GaussianBlur(depth2, (5, 5), 0)

        cv2.imshow('depth4', depth4)
        # cv2.imshow('depth', depth)
        cv2.imshow('blur', blur)  # OK
        k = cv2.waitKey(5)  # & 0xFF
        if k == 27:
            break
except KeyboardInterrupt:
    freenect.sync_stop()
    # freenect.close_device()
