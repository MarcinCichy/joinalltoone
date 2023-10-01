# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_join_all_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
import fnmatch
import pathlib
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QRadioButton, QGroupBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

global file_type                # deklaracje zmiennej globalnej, aby była widoczna we wszystkich metodach
file_type = 'py'

path = pathlib.Path.cwd()


class Ui_MainWindow(object):
    def __init__(self):
        self.icons_list = None
        self.icon_index = 0
        self.icons = None
        self.status_item = {}
        self.all_files_content = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 111, 81))
        self.groupBox.setObjectName("groupBox")
        self.radioButtonPyFile = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonPyFile.setGeometry(QtCore.QRect(10, 20, 82, 18))
        self.radioButtonPyFile.setObjectName("radioButtonPyFile")
        self.radioButtonOtherFile = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonOtherFile.setGeometry(QtCore.QRect(10, 40, 82, 18))
        self.radioButtonOtherFile.setObjectName("radioButtonOtherFile")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 41, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 10, 611, 471))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 571, 421))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(750, 10, 281, 471))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 251, 431))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 500, 91, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  dot. sygnałów przycisku do otwierania okna dialogowego  z wyborem pliku
        self.pushButton.clicked.connect(self.open_file_dialog)
        #self.pushButton_2.clicked.connect(self.show_file_content)
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "File Extension"))
        self.radioButtonPyFile.setText(_translate("MainWindow", "PY"))
        self.radioButtonOtherFile.setText(_translate("MainWindow", "Other"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Joined All Files"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Files to Select"))
        self.pushButton.setText(_translate("MainWindow", "Select Folder"))
        self.pushButton_2.setText(_translate("MainWindow", "JOIN"))

    def open_file_dialog(self):
        self.status_item = {}
        self.textEdit.clear()
        self.listWidget.clear()
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(None, 'Wybierz Folder')

        for file_name in os.listdir(folderpath):
            if fnmatch.fnmatch(file_name, '*.' + file_type):
                item = QtWidgets.QListWidgetItem(file_name)
                item.setIcon(QIcon("red_checkmark.png"))
                self.status_item[item.text()] = False
                self.listWidget.addItem(item)

    def on_item_clicked(self, item):
        current_status = self.status_item.get(item.text(), False)
        new_status = not current_status
        self.status_item[item.text()] = new_status
        self.change_icon(new_status, item)
        self.file_content(new_status, item)
        self.show_file_content(new_status, item)

    # @staticmethod
    def change_icon(self, new_status, item):
        if not new_status:
            item.setIcon(QIcon("red_checkmark.png"))
        else:
            item.setIcon(QIcon("green_checkmark.png"))

    def join_files(self):
        pass

    def file_content(self, new_status, item):
        if new_status:
            with open(item.text(), 'r', encoding='utf-8') as file:
                file_lines = file.readlines()
                self.all_files_content[item.text()] = file_lines
                # print(self.all_files_content)

        elif not new_status:
            del self.all_files_content[item.text()]
            # print(self.all_files_content)

    def show_file_content(self, new_status, item):
        if new_status:
            self.textEdit.insertPlainText(f"FILE: {item.text()} \n\n")
            file_content_list = self.all_files_content.get(item.text(), [])
            content_str = ''.join(file_content_list)
            self.textEdit.insertPlainText(content_str + '\n')
        # elif not new_status:
        #     self.textEdit.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
