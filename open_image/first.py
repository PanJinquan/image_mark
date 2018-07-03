# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 343)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 531, 271))
        self.label.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.openimage)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "打开图片"))
        self.pushButton.setText(_translate("Form", "打开图片"))

