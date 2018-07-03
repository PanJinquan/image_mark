# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_layout2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 210, 101, 84))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.radioButton_1.clicked['bool'].connect(Form.radio_click)
        self.radioButton_2.clicked['bool'].connect(Form.radio_click)
        self.radioButton_3.clicked['bool'].connect(Form.radio_click)
        self.radioButton_4.clicked['bool'].connect(Form.radio_click)
        self.pushButton.clicked.connect(Form.clear_state)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton_1.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.radioButton_3.setText(_translate("Form", "RadioButton"))
        self.radioButton_4.setText(_translate("Form", "RadioButton"))
        self.pushButton.setText(_translate("Form", "PushButton"))

