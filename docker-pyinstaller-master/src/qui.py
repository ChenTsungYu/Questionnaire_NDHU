# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Questionnaire.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(907, 533)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 170, 221, 21))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("輸入學號")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 170, 51, 20))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 210, 221, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText("輸入選課密碼")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 260, 161, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 121, 16))
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(440, 10, 451, 521))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自動填寫教學意見"))
        self.label.setText(_translate("Dialog", "學號 ："))
        self.label_3.setText(_translate("Dialog", "選課密碼："))
        self.label_2.setText(_translate("Dialog", "輸入時請注意英文字大小寫"))
        self.pushButton.setText(_translate("Dialog", "登入"))
        self.label_4.setText(_translate("Dialog", "歡迎使用本工具"))
