import cv2
import numpy as np


def plate_locate(img):
    print('这里是车牌定位')
    img = cv2.GaussianBlur(img, (3, 3), 0)  # 高斯模糊去噪点
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 这个模型中颜色的参数分别是：色调（H），饱和度（S），明度（V）。
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([124, 255, 255])      # 阈值元组，用于蓝色车牌二值化参数
    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # inRange()函数可实现二值化功能（这点类似threshold()函数）通过调节图像颜色信息（H）、饱和度（S）、亮度（V）区间选择我们需要的图像区域：
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    erosion = cv2.dilate(erosion, kernel, iterations=1)
    erosion = cv2.dilate(erosion, kernel, iterations=1)
    contours, hier = cv2.findContours(erosion, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    area = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if (w/h >= 2 and w/h <= 4):
            if w*h > area and area < 1750:
                plate = img[y:y+h, x:x+w]
                area = w*h
    return plate
