# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\vsworkspace\license plate\real\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import cv2
import lct
import tcl
import rec
import idf
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 342)
        self.startDetect = QtWidgets.QPushButton(Form)
        self.startDetect.setEnabled(True)
        self.startDetect.setGeometry(QtCore.QRect(380, 250, 101, 31))
        self.startDetect.setObjectName("startDetect")
        self.startDetect.clicked.connect(self.detect)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 250, 71, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(70, 250, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(260, 250, 31, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.open_file)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 241, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../test/plate9.JPG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 31, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../stander/gan.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 31, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../stander/F.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(340, 60, 31, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../stander/5.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(370, 60, 31, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../stander/3.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(400, 60, 31, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../stander/3.jpg"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(430, 60, 31, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../stander/1.jpg"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(460, 60, 31, 51))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../stander/7.jpg"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(280, 150, 101, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)

        self.label_12.setGeometry(QtCore.QRect(380, 150, 121, 31))
        self.label_12.setTextFormat(QtCore.Qt.RichText)
        self.label_12.setScaledContents(False)
        self.label_12.setIndent(-1)
        self.label_12.setOpenExternalLinks(False)
        self.label_12.setObjectName("label_12")
        self.records = []
        self.file = []

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open_file(self):
        _translate = QtCore.QCoreApplication.translate
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, '选取文件', '.', 'Image Files(*.jpg *.png)')
        self.img_path = fileName
        self.label_2.setPixmap(QtGui.QPixmap(self.img_path))
        self.comboBox.addItem(fileName)
        self.label_12.setText(_translate("Form", ""))

    def isrepeat(self, record):
        for i in range(len(self.records)):
            if record == self.records[i]:
                self.records.remove(self.records[i])

    def write(self):
        f = open("D:/vsworkspace/license plate/real/records.txt", "w", encoding='utf-8')
        for i in self.file:
            f.write(i)
        f.close()

    def detect(self):
        _translate = QtCore.QCoreApplication.translate
        num_list = []
        img = cv2.imread(self.img_path, 1)
        num = self.carnumdet(img)  # 数字获取
        for i in range(len(num)):
            num_list.append(str(num[i][0]))
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        char = ''.join(num_list)
        record = str(char)   # 当前识别结果
        if record in self.records:  # 判断是否重复记录以判断进出
            record_state = record+cur_time+'  out   '
            self.isrepeat(record)
        else:
            record_state = record+cur_time+'   in  '
            self.records.append(record)
        self.file.append(record_state)
        self.write()
        print(self.file)
        self.label_12.setText(_translate("Form", char))
        self.label_4.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number0.jpg"))
        self.label_5.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number1.jpg"))
        self.label_6.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number2.jpg"))
        self.label_7.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number3.jpg"))
        self.label_8.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number4.jpg"))
        self.label_9.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number5.jpg"))
        self.label_10.setPixmap(QtGui.QPixmap("D:/vsworkspace/license plate/Data/number6.jpg"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "车牌识别系统"))
        self.startDetect.setText(_translate("Form", "检测"))
        self.label.setText(_translate("Form", "选择图片："))
        self.toolButton.setText(_translate("Form", "导入"))
        self.label_3.setText(_translate("Form", "切割所得图片："))
        self.label_11.setText(_translate("Form", "车牌号识别结果："))
        self.label_12.setText(_translate("Form", ""))

    def carnumdet(self, img):
        number = []
        # 车牌识别框架开始搭建2020 11 8 9 57
        # 图像预处理：去除噪点，图像归一
        # afterimg = pre.img_preprocess(img)
        # 车牌定位：灰度化，去噪点，背景分割，轮廓检测，开闭运算，hsv模型
        plate = lct.plate_locate(img)
        # 结合数学形态法进一步截取车牌区域
        plate = tcl.get_plate(plate)
        # 获取图片后对其进行水平切割，垂直切割
        self.char_list = rec.plate_split(plate)
        # 对分割好的字符进行特征提取，再识别
        number = idf.idf(self.char_list)
        return number


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
