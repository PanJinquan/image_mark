# -*- coding: utf-8 -*-
import sys
import glob
from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QApplication,QMessageBox
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog,QListWidgetItem,QVBoxLayout
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

from main_layout2 import Ui_Form   # 导入生成first.py里生成的类
from image_storage import ImageStorage
import sys
import  os

class mywindow(QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.curr_index=0  #当前显示的图片
        self.image_list=[] #图片列表
        self.img_stor=ImageStorage()#

    def radio_click(self):
        if self.radioButton_1.isChecked():
            self.image_label=1
        elif self.radioButton_2.isChecked():
            self.image_label=2
        elif self.radioButton_3.isChecked():
            self.image_label=3
        elif self.radioButton_4.isChecked():
            self.image_label=4


    def set_radio_status(self,status):
        self.radioButton_1.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)

    def clear_state(self):
        print("state=",self.radioButton_1.isChecked())
        self.set_radio_status(False)
        # self.radioButton_1.setCheckable(False)
        self.radioButton_1.setAutoExclusive(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_1.setAutoExclusive(True)

        # self.radioButton_1.show()
        print("state=",self.radioButton_1.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())