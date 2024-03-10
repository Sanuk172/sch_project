from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Ui_FormB(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(528, 608)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.book_lvl1_btn = QtWidgets.QPushButton(Form)
        self.book_lvl1_btn.setObjectName("book_lvl1_btn")
        self.verticalLayout.addWidget(self.book_lvl1_btn)
        self.book_lvl2_btn = QtWidgets.QPushButton(Form)
        self.book_lvl2_btn.setObjectName("book_lvl2_btn")
        self.verticalLayout.addWidget(self.book_lvl2_btn)
        self.book_lvl3_btn = QtWidgets.QPushButton(Form)
        self.book_lvl3_btn.setObjectName("book_lvl3_btn")
        self.verticalLayout.addWidget(self.book_lvl3_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout.addWidget(self.back_btn)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.listView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.book_lvl1_btn.setText(_translate("Form", "Учебник 1"))
        self.book_lvl2_btn.setText(_translate("Form", "Учебник  2"))
        self.book_lvl3_btn.setText(_translate("Form", "Учебник 3"))
        self.back_btn.setText(_translate("Form", "Назад"))


