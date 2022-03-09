import cv2
import numpy as np


def img_preprocess(img):
    print("这是预处理")
    height = img.shape[0]
    width = img.shape[1]
    img = cv2.GaussianBlur(img, (3, 3), 0)  # 高斯模糊去噪点
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    sobel = cv2.Sobel(thresh, cv2.CV_16S, 1, 0, ksize=1)  # 垂直边缘检测sobel算子
    sobel = cv2.convertScaleAbs(sobel)
    ret, sobel = cv2.threshold(sobel, 127, 255, cv2.THRESH_OTSU)
    kernel = np.ones((1, 5), np.uint8)
    kernel2 = np.ones((5, 1), np.uint8)
    erosion = cv2.dilate(sobel, kernel, iterations=2)
    erosion = cv2.erode(erosion, kernel, iterations=1)
    erosion = cv2.dilate(erosion, kernel2, iterations=1)
    contours, hier = cv2.findContours(erosion, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    area = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if (w/h >= 2 and w/h <= 4):
            if w*h > area and area < 2000:
                plate = img[y:y+h, x:x+w]
                area = w*h
    cv2.imshow('sobel', sobel)
    cv2.imshow('plate', plate)
    cv2.imshow('img', img)
    cv2.imshow('erosion', erosion)
    cv2.waitKey()
    cv2.destroyAllWindows()
    plate = img[int(height/2):height][0:width]
    return plate
