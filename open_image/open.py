# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
import sys
import glob
from first import Ui_Form   # 导入生成first.py里生成的类
from PyQt5.QtWidgets import QFileDialog
class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        #定义槽函数
    def openimage(self):
   # 打开文件路径
   #设置文件扩展名过滤,注意用双分号间隔
        # imgName,imgType= QFileDialog.getOpenFileName(self,"打开图片",""," *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        dir_path = QFileDialog.getExistingDirectory(self, "choose directory", "C:/Users/Administrator/Desktop")
        image_list=glob.glob(dir_path+'/*.jpg')
        print(image_list)
        #利用qlabel显示图片
        imgName=image_list[0]
        png = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)
app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
