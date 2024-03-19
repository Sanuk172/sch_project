from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 99)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setObjectName("ok")
        self.verticalLayout.addWidget(self.ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ok.setText(_translate("Form", "OK"))
