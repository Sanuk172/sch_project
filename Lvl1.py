# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lvl1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 503)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lvl1_btn = QtWidgets.QPushButton(Form)
        self.lvl1_btn.setObjectName("lvl1_btn")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.lvl1_btn)
        self.verticalLayout.addWidget(self.lvl1_btn)
        self.lvl2_btn = QtWidgets.QPushButton(Form)
        self.lvl2_btn.setObjectName("lvl2_btn")
        self.buttonGroup.addButton(self.lvl2_btn)
        self.verticalLayout.addWidget(self.lvl2_btn)
        self.lvl3_btn = QtWidgets.QPushButton(Form)
        self.lvl3_btn.setObjectName("lvl3_btn")
        self.buttonGroup.addButton(self.lvl3_btn)
        self.verticalLayout.addWidget(self.lvl3_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout.addWidget(self.back_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.send = QtWidgets.QPushButton(Form)
        self.send.setObjectName("send")
        self.verticalLayout_2.addWidget(self.send)
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_2.addWidget(self.error_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lvl1_btn.setText(_translate("Form", "Волшебное число"))
        self.lvl2_btn.setText(_translate("Form", "Волшебный попугай"))
        self.lvl3_btn.setText(_translate("Form", "Магическая сумма чисел"))
        self.back_btn.setText(_translate("Form", "Назад"))
        self.label.setText(_translate("Form", ""))
        self.send.setText(_translate("Form", "Отправить решение"))
        self.error_label.setText(_translate("Form", ""))
