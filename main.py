# -*- coding: utf-8 -*-
import sys
import glob
from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QApplication,QMessageBox
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog,QListWidgetItem,QVBoxLayout
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

from main_layout import Ui_Form   # 导入生成first.py里生成的类
import sys
import  os

class mywindow(QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.curr_index=0
    #显示图片函数
    def show_image(self,image):
        png = QtGui.QPixmap(image).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)
    #图像图片路径列表
    def show_image_list(self,items):
        # 创建列表项
        # conLayout = QVBoxLayout()
        listItem = []
        for lst in items:
            listItem.append(QListWidgetItem(self.tr(lst)))
        # 把列表项添加到listwidget中
        for i in range(len(listItem)):
            self.listWidget.insertItem(i + 1, listItem[i])
        self.listWidget.setCurrentRow(0)#默认选项
        self.listWidget.itemClicked.connect(self.clickitem)

    def clickitem(self,obj):
        self.curr_index=self.listWidget.currentIndex().row()
        print("curr_index= %d,text= %s"%(self.curr_index,obj.text()))
        self.show_image(self.image_list[self.curr_index])
        # QMessageBox.warning(self,"警告",obj.text(),QMessageBox.Yes)

    def open_picture(self):
        # 打开文件路径
        #设置文件扩展名过滤,注意用双分号间隔
        # imgName,imgType= QFileDialog.getOpenFileName(self,"打开图片",""," *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        dir_path = QFileDialog.getExistingDirectory(self, "choose directory",os.getcwd() )
        # self.image_list=glob.glob(dir_path+'/*.jpg')
        self.image_list=glob.glob( os.path.join(dir_path,'*.jpg'))
        print(self.image_list)
        self.show_image(self.image_list[self.curr_index])
        self.show_image_list( self.image_list)

    def up_picture(self):
        self.curr_index -= 1
        if self.curr_index<=0:
            self.curr_index=0
        print("curr_index=",self.curr_index)
        self.listWidget.setCurrentRow(self.curr_index)#被选中的选项
        self.show_image(self.image_list[self.curr_index])

    def next_picture(self):
        self.curr_index += 1
        if self.curr_index>=len(self.image_list)-1:
            self.curr_index=len(self.image_list)-1
        print("curr_index=",self.curr_index)
        self.listWidget.setCurrentRow(self.curr_index)#被选中的选项
        self.show_image(self.image_list[self.curr_index])

    def radio_click(self):
        if self.radioButton_1.isChecked():
            self.image_label=1
        elif self.radioButton_2.isChecked():
            self.image_label=2
        elif self.radioButton_3.isChecked():
            self.image_label=3
        elif self.radioButton_4.isChecked():
            self.image_label=4
        elif self.radioButton_5.isChecked():
            self.image_label=5
        print('image_label=', self.image_label)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())