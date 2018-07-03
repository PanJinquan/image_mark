# -*- coding: utf-8 -*-
import sys
import glob
from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QApplication,QMessageBox
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog,QListWidgetItem,QVBoxLayout
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from main_layout import Ui_Form   # 导入生成first.py里生成的类
from image_storage import ImageStorage
import sys
import  os

class mywindow(QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.out_path=os.getcwd()
        self.curr_index=0  #当前显示的图片
        self.image_list=[] #图片列表
        self.image_label=[] #图片列表
        self.img_stor=ImageStorage()#
    #显示图片函数
    def show_image(self,image_path):
        png = QtGui.QPixmap(image_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)
    def PRINT_DEBUG(self):
        label=self.image_label[self.curr_index]
        curr_image=self.image_list[self.curr_index]
        print("curr_index=",self.curr_index,'curr_image=',curr_image,'image_label=',self.image_label)
        image_name = os.path.basename(curr_image)
        info="curr_index="+str(self.curr_index)+',curr_label='+str(label)+',curr_image='+image_name
        self.setTextBrowser(info)
        # print("curr_index=",self.curr_index,'curr_image=',curr_image,'curr_label=',label)
    #图像图片路径列表
    def show_image_list(self,items):
        # 创建列表项
        # conLayout = QVBoxLayout()
        listItem = []
        self.listWidget.clear()
        for lst in items:
            listItem.append(QListWidgetItem(self.tr(lst)))
        # 把列表项添加到listwidget中
        for i in range(len(listItem)):
            self.listWidget.insertItem(i + 1, listItem[i])
        self.listWidget.setCurrentRow(0)#默认选项
        self.listWidget.itemClicked.connect(self.clickitem)
    def set_image_list_status(self):
        self.listWidget.item(self.curr_index).setBackground(QColor(187,255,255))
        # self.listWidget.item(self.curr_index).setTextColor(QColor(190,190,190))


    def clickitem(self,obj):
        self.curr_index=self.listWidget.currentIndex().row()
        # print("clickitem text=",obj.text())#获得选项的内容
        self.show_image(self.image_list[self.curr_index])#显示被点击的图片
        # QMessageBox.warning(self,"警告",obj.text(),QMessageBox.Yes)
        self.PRINT_DEBUG()
        label=self.image_label[self.curr_index]
        self.clear_radio_status()
        if label!=0:
            self.set_radio_status(label,True)

    def open_picture(self):
        # 打开文件路径
        #设置文件扩展名过滤,注意用双分号间隔
        # imgName,imgType= QFileDialog.getOpenFileName(self,"打开图片",""," *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        dir_path = QFileDialog.getExistingDirectory(self, "choose images dir",os.getcwd() )
        # self.image_list=glob.glob(dir_path+'/*.jpg')
        self.image_list=glob.glob( os.path.join(dir_path,'*.jpg'))
        if len(self.image_list) == 0:
            print("Err:no images...")
            self.setTextBrowser("Err:no images...")
            return
        self.setTextBrowser("info:load images...,num="+str(len(self.image_list)))
        self.image_label = [0] * len( self.image_list)
        self.show_image(self.image_list[self.curr_index])
        self.show_image_list( self.image_list)

    def open_save(self):
        self.out_path = QFileDialog.getExistingDirectory(self, "choose save data dir",os.getcwd() )


    def up_picture(self):
        if len(self.image_list)==0:
            self.curr_index = 0
            return
        self.curr_index -= 1
        if self.curr_index<=0:
            self.curr_index=0
        self.listWidget.setCurrentRow(self.curr_index)#被选中的选项
        self.show_image(self.image_list[self.curr_index])
        label=self.image_label[self.curr_index]
        self.PRINT_DEBUG()
        self.clear_radio_status()
        if label!=0:
            self.set_radio_status(label,True)


    def next_picture(self):
        if len(self.image_list)==0:
            self.curr_index = 0
            return
        self.curr_index += 1
        if self.curr_index>=len(self.image_list)-1:
            self.curr_index=len(self.image_list)-1
        self.listWidget.setCurrentRow(self.curr_index)#被选中的选项
        self.show_image(self.image_list[self.curr_index])
        label=self.image_label[self.curr_index]
        self.PRINT_DEBUG()
        self.clear_radio_status()
        if label!=0:
            self.set_radio_status(label,True)

    def radio_click(self):
        if len(self.image_list)==0:
            self.curr_index = 0
            return
        if self.radioButton_1.isChecked():
            label=1
        elif self.radioButton_2.isChecked():
            label=2
        elif self.radioButton_3.isChecked():
            label=3
        elif self.radioButton_4.isChecked():
            label=4
        elif self.radioButton_5.isChecked():
            label=5
        self.set_image_list_status()#改变字体颜色，表示已经选择
        self.image_label[self.curr_index]=label
        image_path=self.image_list[self.curr_index]
        # image_name=image_path.split('/')[-1]
        image_name = os.path.basename(image_path)
        txt_data=[]
        txt_data.append([image_name,label])
        txt_filename=os.path.splitext(image_name)[0]+".txt"
        txt_filename=os.path.join(self.out_path,txt_filename)
        print('image_name=%s,image_label=%d'%(image_name,label))
        self.PRINT_DEBUG()
        self.img_stor.save_txt(txt_data,txt_filename,mode='w')

    def set_radio_status(self,label,status):
        if label==1:
            self.radioButton_1.setAutoExclusive(False)
            self.radioButton_1.setChecked(status)
            self.radioButton_1.setAutoExclusive(True)
        elif label==2:
            self.radioButton_2.setAutoExclusive(False)
            self.radioButton_2.setChecked(status)
            self.radioButton_2.setAutoExclusive(True)
        elif label==3:
            self.radioButton_3.setAutoExclusive(False)
            self.radioButton_3.setChecked(status)
            self.radioButton_3.setAutoExclusive(True)
        elif label==4:
            self.radioButton_4.setAutoExclusive(False)
            self.radioButton_4.setChecked(status)
            self.radioButton_4.setAutoExclusive(True)
        elif label==5:
            self.radioButton_5.setAutoExclusive(False)
            self.radioButton_5.setChecked(status)
            self.radioButton_5.setAutoExclusive(True)

    def clear_radio_status(self):
        status=False
        if self.radioButton_1.isChecked():
            self.radioButton_1.setAutoExclusive(False)
            self.radioButton_1.setChecked(status)
            self.radioButton_1.setAutoExclusive(True)
        elif self.radioButton_2.isChecked():
            self.radioButton_2.setAutoExclusive(False)
            self.radioButton_2.setChecked(status)
            self.radioButton_2.setAutoExclusive(True)
        elif self.radioButton_3.isChecked():
            self.radioButton_3.setAutoExclusive(False)
            self.radioButton_3.setChecked(status)
            self.radioButton_3.setAutoExclusive(True)
        elif self.radioButton_4.isChecked():
            self.radioButton_4.setAutoExclusive(False)
            self.radioButton_4.setChecked(status)
            self.radioButton_4.setAutoExclusive(True)
        elif self.radioButton_5.isChecked():
            self.radioButton_5.setAutoExclusive(False)
            self.radioButton_5.setChecked(status)
            self.radioButton_5.setAutoExclusive(True)

    def setTextBrowser(self,content):
        self.textBrowser.clear()
        self.textBrowser.append(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())