import cv2
import numpy as np


def get_plate(plate):
    gray_img = cv2.cvtColor(plate, cv2.COLOR_RGB2GRAY)
    canny = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0, ksize=1)
    canny = cv2.convertScaleAbs(canny)
    ret, canny = cv2.threshold(canny, 0, 255, cv2.THRESH_OTSU)
    kernel = np.ones((1, 20), np.uint8)
    kernel2 = np.ones((5, 1), np.uint8)
    kernel3 = np.ones((5, 5), np.uint8)
    erosion = cv2.dilate(canny, kernel, iterations=1)
    erosion = cv2.erode(erosion, kernel2, iterations=1)
    erosion = cv2.dilate(erosion, kernel3, iterations=1)
    # cv2.imshow("erosion", erosion)
    contours, hier = cv2.findContours(erosion, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    area = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        # img = cv2.rectangle(plate, (x, y), (x+w, y+h), (195, 255, 25), 1)
        if w*h > area:
            g_plate = plate[y:y+h, x:x+w]
            area = w*h
    # cv2.imshow("canny", canny)
    # cv2.imshow("imf", img)
    # cv2.imshow("plate", g_plate)
    return g_plate
