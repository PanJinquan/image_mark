# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 548)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 20, 401, 401))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 430, 54, 12))
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(Form)
        self.radioButton_1.setGeometry(QtCore.QRect(160, 430, 89, 16))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 450, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 470, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(160, 490, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(160, 510, 89, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 470, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 500, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 530, 54, 12))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 101, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.open_picture)
        self.pushButton_2.clicked.connect(Form.up_picture)
        self.pushButton_3.clicked.connect(Form.next_picture)
        self.radioButton_1.clicked.connect(Form.radio_click)
        self.radioButton_2.clicked.connect(Form.radio_click)
        self.radioButton_3.clicked.connect(Form.radio_click)
        self.radioButton_4.clicked.connect(Form.radio_click)
        self.radioButton_5.clicked.connect(Form.radio_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "评分："))
        self.radioButton_1.setText(_translate("Form", "1"))
        self.radioButton_2.setText(_translate("Form", "2"))
        self.radioButton_3.setText(_translate("Form", "3"))
        self.radioButton_4.setText(_translate("Form", "4"))
        self.radioButton_5.setText(_translate("Form", "5"))
        self.pushButton.setText(_translate("Form", "打开照片"))
        self.pushButton_2.setText(_translate("Form", "上一张"))
        self.pushButton_3.setText(_translate("Form", "下一张"))
        self.label_3.setText(_translate("Form", "状态："))

