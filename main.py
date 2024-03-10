import os
import shutil
import sys

from PyQt5 import QtCore

from data.book import Ui_FormB
from data.first_page import Ui_MainWindow
from data.Lvl1 import Ui_Form1
from data.Lvl2 import Ui_Form2
from data.Lvl3 import Ui_Form3
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAbstractItemView

level1 = {
        "Волшебное число": {'text': '',
                            'verdict': ''},

        "Волшебный попугай": {'text': '',
                              'verdict': ''},

        "Магическая сумма чисел": {'text': '',
                                   'verdict': ''}
}
level2 = {
        "Поиск маны": {'text': '',
                       'verdict': ''},

        "Сильнее среднего": {'text': '',
                             'verdict': ''},

        "Четное нечетное": {'text': '',
                            'verdict': ''}
}
level3 = {
        "Множества": {'text': '',
                      'verdict': ''},

        "Словари": {'text': '',
                    'verdict': ''},

        "Списки": {'text': '',
                   'verdict': ''
                   }
}
level1_tests = {
        "Волшебное число": 'test_1',

        "Волшебный попугай": 'test_2',

        "Магическая сумма чисел": 'test_3'
}
level2_tests = {
        "Поиск маны": 'tests/test_5',

        "Сильнее среднего": 'tests/test_4',

        "Четное нечетное": 'tests/test_6'
}
level3_tests = {
        "Множества": 'test_7',

        "Словари": 'test_8',

        "Списки": 'test_9'
}


class FirstPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.lvl3 = Level3()
        self.lvl2 = Level2()
        self.lvl1 = Level1()
        self.book = Book()
        self.setupUi(self)
        self.click_button()

    def click_button(self):
        self.book_btn.clicked.connect(self.open_book)
        self.lvl1_btn.clicked.connect(self.open_lvl1)
        self.lvl2_btn.clicked.connect(self.open_lvl2)
        self.lvl3_btn.clicked.connect(self.open_lvl3)

    def open_book(self):
        self.hide()
        self.book.showMaximized()

    def open_lvl1(self):
        self.hide()
        self.lvl1.showMaximized()

    def open_lvl2(self):
        self.hide()
        self.lvl2.showMaximized()

    def open_lvl3(self):
        self.hide()
        self.lvl3.showMaximized()


class Book(QWidget, Ui_FormB):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click_button()

    def click_button(self):
        self.back_btn.clicked.connect(self.back)
        self.book_lvl1_btn.clicked.connect(self.open_book_lvl1)
        self.book_lvl2_btn.clicked.connect(self.open_book_lvl2)
        self.book_lvl3_btn.clicked.connect(self.open_book_lvl3)

    def open_book_lvl1(self):
        self.model = QStandardItemModel(self)
        self.listView.setModel(self.model)
        with open('data/books/Book1.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            i = i.rstrip()
            item = QStandardItem(i)
            item.setData(i)
            self.model.appendRow(item)
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def open_book_lvl2(self):
        self.model = QStandardItemModel(self)
        self.listView.setModel(self.model)
        with open('data/books/Book2.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            i = i.rstrip()
            item = QStandardItem(i)
            item.setData(i)
            self.model.appendRow(item)
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def open_book_lvl3(self):
        self.model = QStandardItemModel(self)
        self.listView.setModel(self.model)
        with open('data/books/Book3.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            i = i.rstrip()
            item = QStandardItem(i)
            item.setData(i)
            self.model.appendRow(item)
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def back(self):
        self.main = FirstPage()
        self.hide()
        self.main.show()


class Level1(QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click_button()
        self.textEdit.textChanged.connect(self.save_to)

        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        for filename in os.listdir('data/tmp_files'):
            file_path = os.path.join('data/tmp_files', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def click_button(self):
        self.send.clicked.connect(self.send_decision)
        self.back_btn.clicked.connect(self.back)
        self.buttonGroup.buttonClicked.connect(self.load_lvl)

    def uslovie(self, name):
        stroka = ''
        with open(f"data/tasks/{name}.txt", 'r', encoding='utf-8') as f:
            f = f.readlines()
            for i in f:
                stroka += i
        self.label.setText(stroka.rstrip())

    def load_lvl(self, button):
        self.btn_name = button.text()
        self.uslovie(self.btn_name)
        self.error_label.setText(level1[self.btn_name]['verdict'])
        self.textEdit.setText(level1[self.btn_name]['text'])

    def save_to(self):
        self.text = self.textEdit.toPlainText()
        level1[self.btn_name]['text'] = self.text
        with open(f'data/tmp_files/{self.btn_name}.py', 'w', encoding='utf-8') as decision:
            decision.write(self.text)

    def send_decision(self):
        self.process.start('python', [f'data/tests/{level1_tests[self.btn_name]}.py'])
        if 'OK' in self.verdict:
            self.verdict = 'Зачтено'
        else:
            self.verdict = 'Доработать' + self.verdict

        level1[self.btn_name]['verdict'] = self.verdict
        self.error_label.setText(self.verdict)

    def keyPressEvent(self, event) -> None:
        if event:
            self.text = self.textEdit.toPlainText()

    def back(self):
        self.main = FirstPage()
        self.hide()
        self.main.show()

    def stdoutReady(self):
        out = self.process.readAllStandardOutput()
        self.verdict = str(out, 'utf-8')

    def stderrReady(self):
        err = self.process.readAllStandardError()
        self.verdict = str(err, 'utf-8')


class Level2(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click_button()
        self.textEdit.textChanged.connect(self.save_to)

        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        for filename in os.listdir('data/tmp_files'):
            file_path = os.path.join('data/tmp_files', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def click_button(self):
        self.send.clicked.connect(self.send_decision)
        self.back_btn.clicked.connect(self.back)
        self.buttonGroup.buttonClicked.connect(self.load_lvl)

    def uslovie(self, name):
        stroka = ''
        with open(f"data/tasks/{name}.txt", 'r', encoding='utf-8') as f:
            f = f.readlines()
            for i in f:
                stroka += i
        self.label.setText(stroka.rstrip())

    def load_lvl(self, button):
        self.btn_name = button.text()
        self.uslovie(self.btn_name)
        self.error_label.setText(level1[self.btn_name]['verdict'])
        self.textEdit.setText(level1[self.btn_name]['text'])

    def save_to(self):
        self.text = self.textEdit.toPlainText()
        level1[self.btn_name]['text'] = self.text
        with open(f'data/tmp_files/{self.btn_name}.py', 'w', encoding='utf-8') as decision:
            decision.write(self.text)

    def send_decision(self):
        self.process.start('python', [f'data/tests/{level2_tests[self.btn_name]}.py'])
        if 'OK' in self.verdict:
            self.verdict = 'Зачтено'
        else:
            self.verdict = 'Доработать' + self.verdict

        level1[self.btn_name]['verdict'] = self.verdict
        self.error_label.setText(self.verdict)

    def keyPressEvent(self, event) -> None:
        if event:
            self.text = self.textEdit.toPlainText()

    def back(self):
        self.main = FirstPage()
        self.hide()
        self.main.show()

    def stdoutReady(self):
        out = self.process.readAllStandardOutput()
        self.verdict = str(out, 'utf-8')

    def stderrReady(self):
        err = self.process.readAllStandardError()
        self.verdict = str(err, 'utf-8')


class Level3(QWidget, Ui_Form3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click_button()
        self.textEdit.textChanged.connect(self.save_to)

        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        for filename in os.listdir('data/tmp_files'):
            file_path = os.path.join('data/tmp_files', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def click_button(self):
        self.send.clicked.connect(self.send_decision)
        self.back_btn.clicked.connect(self.back)
        self.buttonGroup.buttonClicked.connect(self.load_lvl)

    def uslovie(self, name):
        stroka = ''
        with open(f"data/tasks/{name}.txt", 'r', encoding='utf-8') as f:
            f = f.readlines()
            for i in f:
                stroka += i
        self.label.setText(stroka.rstrip())

    def load_lvl(self, button):
        self.btn_name = button.text()
        self.uslovie(self.btn_name)
        self.error_label.setText(level1[self.btn_name]['verdict'])
        self.textEdit.setText(level1[self.btn_name]['text'])

    def save_to(self):
        self.text = self.textEdit.toPlainText()
        level1[self.btn_name]['text'] = self.text
        with open(f'data/tmp_files/{self.btn_name}.py', 'w', encoding='utf-8') as decision:
            decision.write(self.text)

    def send_decision(self):
        self.process.start('python', [f'data/tests/{level3_tests[self.btn_name]}.py'])
        if 'OK' in self.verdict:
            self.verdict = 'Зачтено'
        else:
            self.verdict = 'Доработать' + self.verdict

        level1[self.btn_name]['verdict'] = self.verdict
        self.error_label.setText(self.verdict)

    def keyPressEvent(self, event) -> None:
        if event:
            self.text = self.textEdit.toPlainText()

    def back(self):
        self.main = FirstPage()
        self.hide()
        self.main.show()

    def stdoutReady(self):
        out = self.process.readAllStandardOutput()
        self.verdict = str(out, 'utf-8')

    def stderrReady(self):
        err = self.process.readAllStandardError()
        self.verdict = str(err, 'utf-8')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstPage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
