import cv2
import numpy as np


def plate_split(plate):
    print("这是车牌修正与分割")
    # 图像归一化、中值滤波、图像效果增强、二值化、方向矫正以及去除大噪点的二值图像后处理
    gray_plate = cv2.cvtColor(plate, cv2.COLOR_RGB2GRAY)
    # 车牌归一化
    cns_plate = cv2.resize(gray_plate, (176, 58), interpolation=cv2.INTER_AREA)
    # 中值滤波
    blu_plate = cns_plate
    # 图像增强 灰度拉伸：提高图像处理时灰度级的动态范围
    rows, cols = blu_plate.shape
    flat_gray = blu_plate.reshape((cols * rows,)).tolist()
    A = min(flat_gray)
    B = max(flat_gray)
    print('A = %d,B = %d' % (A, B))
    output = np.uint8(255 / (B - A) * (blu_plate - A) + 0.5)
    # 自适应阈值二值化
    # img_thre = cv2.adaptiveThreshold(output, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    ret, img_thre = cv2.threshold(output, 127, 255, cv2.THRESH_BINARY)
    # kernel2 = np.ones((2, 2), np.uint8)
    s_plate = img_thre  # 保存副本
    kernel1 = np.ones((3, 3), np.uint8)
    # img_thre = cv2.dilate(erosion, kernel1, iterations=1)
    r_point = []  # 记录行分界点
    c_point = []  # 记录列分界点
    height = img_thre.shape[0]
    print(height)
    width = img_thre.shape[1]
    print(width)
    j = 0
    k = 0
    bf_contain = 0
    bef_contain = 0
    white_sum = 0
    top_line = 0
    under_line = height
    char_list = []
    # 倾斜矫正：在图像上应用仿射变换

    # 水平投影分割
    for h in range(height):
        for w in range(width):
            white_sum += img_thre[h][w]
        white_con = white_sum / (255*width)
        if abs(bef_contain-white_con) > 0.2 and (bef_contain < 0.2 or white_con < 0.2):    # 反复调试 百分比为0.2 水平分割效果最佳 去除掉上面的两个铁钉
            bef_contain = white_con
            r_point.append(h)
        white_sum = 0
    for p in range(len(r_point)-1):
        if r_point[p+1]-r_point[p] > 15 and (p+1) < len(r_point):
            top_line = r_point[p]
            under_line = r_point[p+1]
    img_thre = img_thre[top_line:under_line][0:width]
    plate = s_plate[top_line:under_line][0:width]
    if top_line == 0 or under_line == 0:
        print("未获得车牌")
        exit
    img_thre = cv2.dilate(img_thre, kernel1, iterations=0)
    #  垂直投影分割
    height = img_thre.shape[0]
    width = img_thre.shape[1]
    for j in range(width):
        i = 0
        white = 0.0
        for i in range(height):
            white = white+img_thre[i][j]
        white_contain = white/(255*height)
        if abs(bf_contain - white_contain) > 0 and bf_contain * white_contain == 0:
            c_point.append(j)
            img_thre[10][j] = 255
        bf_contain = white_contain
    m = 0
    for k in range(len(c_point)):
        if k % 2 == 0 and k+1 < len(c_point):
            indexl = c_point[k]
            indexr = c_point[k+1]
            if k == 0 and (indexr - indexl) < int(width/12) or (k > len(c_point)-3 and (indexr - indexl) < int(width/12)):
                continue
            char = plate[0:height, indexl:indexr]  # 取坐标点在副本中截取
            if (indexr - indexl) < int(width/12):
                c_width = char.shape[1]
                c_height = char.shape[0]
                p_sum = 0
                for i in range(c_width):
                    for p in range(c_height):
                        p_sum = p_sum+char[p][i]
                prp = p_sum/(c_height*c_width*255)
                if prp < 0.2:
                    continue
            # 字符归一化
            w = round(abs(int(char.shape[0]/2)-char.shape[1])/2)
            char = cv2.copyMakeBorder(char, 4, 4, w, w, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            char = cv2.resize(char, (24, 48), interpolation=cv2.INTER_AREA)
            char_list.append(char)
            dress = 'D:/vsworkspace/license plate/Data/number{bat}.jpg'.format(bat=m)
            m = m+1
            cv2.imwrite(dress, char)
    return char_list
