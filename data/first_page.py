# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(295, 169)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.book_btn = QtWidgets.QPushButton(self.centralwidget)
        self.book_btn.setObjectName("book_btn")
        self.verticalLayout.addWidget(self.book_btn)
        self.lvl1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lvl1_btn.setObjectName("lvl1_btn")
        self.verticalLayout.addWidget(self.lvl1_btn)
        self.lvl2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lvl2_btn.setObjectName("lvl2_btn")
        self.verticalLayout.addWidget(self.lvl2_btn)
        self.lvl3_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lvl3_btn.setObjectName("lvl3_btn")
        self.verticalLayout.addWidget(self.lvl3_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.book_btn.setText(_translate("MainWindow", "Учебник"))
        self.lvl1_btn.setText(_translate("MainWindow", "Уровень 1"))
        self.lvl2_btn.setText(_translate("MainWindow", "Уровень 2"))
        self.lvl3_btn.setText(_translate("MainWindow", "Уровень 3"))
