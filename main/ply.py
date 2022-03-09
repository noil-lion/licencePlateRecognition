import cv2
import numpy as np
import math


def show(A, B):
    E = []
    F = []
    for i in range(len(A)):
        if A[i] != 0:
            E.append(A[i])
    for i in range(len(B)):
        if B[i] != 0:
            F.append(B[i])
    img1 = np.zeros((360, 360), np.uint8)
    img2 = np.zeros((360, 360), np.uint8)
    for i in range(len(E)):
        k = int(abs(E[i]))
        img1[0:k*10, i*10:i*10+10] = 255
    for i in range(len(F)-1):
        k = int(abs(F[i]))-2
        img2[0:k*10, i*10:i*10+10] = 255
    cv2.imshow("E", img1)
    cv2.imshow("F", img2)
    cv2.waitKey()


def calcMean(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)
    x_mean = float(sum_x+0.0)/n
    y_mean = float(sum_y+0.0)/n
    return x_mean, y_mean


def calcPearson(x, y):
    x_mean, y_mean = calcMean(x, y)	 # 计算x,y向量平均值
    n = len(x)
    sumTop = 0.0
    sumBottom = 0.0
    x_pow = 0.0
    y_pow = 0.0
    for i in range(n):
        sumTop += (x[i]-x_mean)*(y[i]-y_mean)
    for i in range(n):
        x_pow += math.pow(x[i]-x_mean, 2)
    for i in range(n):
        y_pow += math.pow(y[i]-y_mean, 2)
    sumBottom = math.sqrt(x_pow*y_pow)
    p = sumTop/sumBottom
    return p


'''if __name__ == "__main__":
    # E = [2.0, 3.0, 3.0, 3.0, 3.0, 2.0, 8.0, 9.0, 12.0, 9.0, 9.0, 8.0, 8.0, 0.0, 6.0, 1.0, 0.0, 7.0, 8.0, 0.0, 7.0, 1.0, 0.0, 8.0, 8.0, 0.0, 5.0, 0.0, 0.0, 8.0, 1.0, 0.0, 0.0, 0.0, 0.0, 2.0]
    # E = [5.0, 7.0, 7.0, 4.0, 2.0, 0.0, 5.0, 10.0, 10.0, 10.0, 10.0, 0.0, 5.0, 0.0, 7.0, 3.0, 3.0, 0.0, 5.0, 0.0, 6.0, 0.0, 0.0, 0.0, 5.0, 0.0, 6.0, 0.0, 0.0, 0.0, 5.0, 0.0, 4.0, 0.0, 0.0, 2.0]
    # F = [4.0, 6.0, 5.0, 0.0, 0.0, 0.0, 7.0, 14.0, 15.0, 15.0, 14.0, 0.0, 7.0, 0.0, 9.0, 5.0, 4.0, 0.0, 7.0, 0.0, 8.0, 0.0, 0.0, 0.0, 7.0, 0.0, 8.0, 0.0, 0.0, 0.0, 7.0, 0.0, 5.0, 0.0, 0.0, 1.0]
    # E = [1.0, 2.0, 2.0, 4.0, 5.0, 2.0, 4.0, 10.0, 10.0, 10.0, 9.0, 4.0, 4.0, 3.0, 0.0, 0.0, 3.0, 4.0, 4.0, 3.0, 0.0, 2.0, 6.0, 4.0, 3.0, 10.0, 10.0, 10.0, 10.0, 1.0, 0.0, 3.0, 2.0, 2.0, 1.0, 0.0]
    F = [0.0, 3.0, 2.0, 4.0, 4.0, 0.0, 2.0, 14.0, 12.0, 15.0, 13.0, 0.0, 5.0, 8.0, 13.0, 5.0, 9.0, 3.0, 5.0, 1.0, 9.0, 2.0, 7.0, 3.0, 5.0, 10.0, 14.0, 8.0, 10.0, 0.0, 0.0, 13.0, 7.0, 15.0, 8.0, 0.0]
    E = [0.0, 6.0, 3.0, 7.0, 5.0, 0.0, 4.0, 10.0, 10.0, 10.0, 10.0, 1.0, 5.0, 5.0, 9.0, 3.0, 7.0, 2.0, 5.0, 1.0, 8.0, 1.0, 6.0, 2.0, 5.0, 9.0, 10.0, 8.0, 9.0, 0.0, 1.0, 10.0, 6.0, 10.0, 5.0, 0.0]
    show(E, F)
    p = calcPearson(E, F)
    print(p)'''
