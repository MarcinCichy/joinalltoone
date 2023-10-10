# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_join_all_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
import fnmatch
import pathlib
from pathlib import Path
from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtGui import QIcon
from OpenFileDialog import OpenFileDialog
from SaveFileDialog import SaveFileDialog

# path = pathlib.Path.cwd()

class Ui_MainWindow(object):
    def __init__(self):
        self.icons_list = None
        self.icon_index = 0
        self.icons = None
        self.status_item = {}
        self.all_files_content = {}
        self.file_type = 'py'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.pushButton_2.setGeometry(QtCore.QRect(140, 500, 91, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 500, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 500, 111, 18))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  signals, sockets and connections
        self.pushButton.clicked.connect(self.open_file_dialog)
        self.pushButton_2.clicked.connect(self.join_files)
        self.pushButton_3.clicked.connect(self.clear_list_of_files)
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        self.radioButtonPyFile.toggled.connect(self.onClicked)
        self.radioButtonOtherFile.toggled.connect(self.onClicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "File Types"))
        self.radioButtonPyFile.setText(_translate("MainWindow", "PY"))
        self.radioButtonOtherFile.setText(_translate("MainWindow", "Other"))
        self.groupBox_2.setTitle(_translate("MainWindow", "All Files Combined"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Files to Select"))
        self.pushButton.setText(_translate("MainWindow", "SELECT FILES"))
        self.pushButton_2.setText(_translate("MainWindow", "JOIN"))
        self.pushButton_3.setText(_translate("MainWindow", "CLEAR"))
        self.checkBox.setText(_translate("MainWindow", "with configuration"))

    def onClicked(self):
        global file_type                                    # ???

        if self.radioButtonOtherFile.isChecked():
            if len(self.lineEdit.text()) != 0:
                self.file_type = (self.lineEdit.text().lower())
            else:
                self.file_type = 'html'
        elif self.radioButtonPyFile.isChecked():
            self.file_type = 'py'
            self.lineEdit.clear()
        return self.file_type

    def open_file_dialog(self):
        self.textEdit.clear()
        open_file_dialog = OpenFileDialog()
        file_paths = open_file_dialog.get_file_path(self.file_type)

        for file_path in file_paths:
            file_name = Path(file_path).name

            if Path(file_name).suffix == ".joined":
                print(file_name)
                with open(file_name, 'r', encoding='utf-8') as file:
                    print(json.load(file))

            else:
                self.all_files_content[file_name] = {'path': file_path, 'content': []}

                if fnmatch.fnmatch(file_name, '*.' + self.file_type):
                    item = QtWidgets.QListWidgetItem(file_name)
                    item.setIcon(QIcon("red_checkmark.png"))
                    self.status_item[item.text()] = False
                    self.listWidget.addItem(item)

    def on_item_clicked(self, item):
        current_status = self.status_item.get(item.text(), False)
        new_status = not current_status
        self.status_item[item.text()] = new_status
        self.change_icon(item)

        if new_status:
            self.file_content(item)
            self.show_file_content()
        elif not new_status:
            self.all_files_content[item.text()]['content'] = []
            self.show_file_content()

    def change_icon(self, item):
        temp1_status = self.status_item.get(item.text(), False)
        if not temp1_status:
            item.setIcon(QIcon("red_checkmark.png"))
        else:
            item.setIcon(QIcon("green_checkmark.png"))

    def file_content(self, item):
        file_to_read = self.all_files_content.get(item.text())
        with open(file_to_read['path'], 'r', encoding='utf-8') as file:
            file_lines = file.readlines()
            file_to_read['content'] = file_lines

    def show_file_content(self):
        self.textEdit.clear()
        for file_name, file_content in self.all_files_content.items():
            if file_content['content']:
                self.textEdit.insertPlainText(f"FILE: {file_name} \n\n")
                content_str = ''.join(file_content['content'])
                self.textEdit.insertPlainText(content_str + '\n\n')

    def join_files(self):
        joined_text = self.textEdit.toPlainText()
        save_file_dialog = SaveFileDialog()
        if self.checkBox.isChecked():
            print(self.all_files_content)
            save_file_dialog.set_file_path(joined_text, self.all_files_content)
        else:
            save_file_dialog.set_file_path(joined_text, None)

    def clear_list_of_files(self):
        self.listWidget.clear()
        self.textEdit.clear()
        self.all_files_content = {}


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
