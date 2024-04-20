# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_join_all_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
from pathlib import Path
import fnmatch
import magic


from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from OpenFileDialog import OpenFileDialog
from SaveFileDialog import SaveFileDialog


class Ui_MainWindow(object):
    def clear_list_of_files(self):
        pass

    def join_files(self):
        pass

    def open_file_dialog(self):
        pass

    def on_item_clicked(self, item):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 535)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(943, 535))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 611, 471))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 571, 421))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(640, 10, 281, 471))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 251, 431))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 500, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 500, 91, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 500, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(120, 500, 111, 18))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  signals, sockets and connections
        self.pushButton.clicked.connect(self.open_file_dialog)
        self.pushButton_2.clicked.connect(self.join_files)
        self.pushButton_3.clicked.connect(self.clear_list_of_files)
        self.listWidget.itemClicked.connect(self.on_item_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Join All Files To One"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Joined All Files"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Files to Select"))
        self.pushButton.setText(_translate("MainWindow", "Select Files"))
        self.pushButton_2.setText(_translate("MainWindow", "JOIN"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.checkBox.setText(_translate("MainWindow", "with layout"))


class FilesJoiner(Ui_MainWindow):
    """
    A class to combine multiple source code files into one file, as follows:
    ====================
    FILE: file name

    file content

    ====================
    FILE: name of the next file

    content of the next file
    """
    def __init__(self):
        super().__init__()
        self.status_item = {}
        self.all_files_content = {}
        self.file_type = 'py'

    def open_file_dialog(self):
        """
        A method used to load the names of a file or files using a dialog box, taking into account the defined file type
         (in this case .py).
        This method also allows you to load a previously saved file layout (.layout file type) in order to continue
        working on them.

        If new files are indicated, they are marked with a red icon.
        If a previously saved file arrangement has been loaded, they receive the same markings
        as they had at the time of saving and the content of the linked file is restored.

        The "all_files_content" dictionary is created, where the names of the files selected in the dialog box
        are inserted as keys. The values are dictionaries containing the keys "path" -> with a value indicating
        the path to the file and the key "content" -> at the moment of creation it has an empty value,
        which is completed when the file is indicated for connection.

        File types with the .layout extension are saved and loaded using JSON.
        """
        self.textEdit.clear()
        open_file_dialog = OpenFileDialog()
        file_paths = open_file_dialog.get_file_path(self.file_type)

        for file_path in file_paths:
            file_name = Path(file_path).name

            if self.is_text_file(file_path):
                if Path(file_name).suffix != ".layout":
                    self.all_files_content[file_name] = {'path': file_path, 'content': []}

                    if fnmatch.fnmatch(file_name, '*.' + self.file_type):
                        item = QtWidgets.QListWidgetItem(file_name)
                        item.setIcon(QIcon("red_checkmark.png"))
                        self.status_item[item.text()] = False
                        self.listWidget.addItem(item)
                else:
                    self.clear_list_of_files()
                    self.all_files_content = self.read_files_layout(file_name)
                    for file_name in self.all_files_content.keys():
                        if self.all_files_content[file_name]['content']:
                            self.status_item[file_name] = True
                        else:
                            self.status_item[file_name] = False
                    self.show_file_content()
            else:
                message = f"This is not a text file"
                self.show_message(message)

    def on_item_clicked(self, item):
        """
        Method that changes the status of a file and its icon after clicking on it (False = not selected, red icon;
        True = selected, green icon).
        Depending on the status, the file content and its name appear in the "Joined All Files" window
        or are removed from it.
        """
        icon_paths = ("green_checkmark.png", "red_checkmark.png")

        new_status = not self.status_item.get(item.text(), False)
        self.status_item[item.text()] = new_status
        self.change_icon(item, new_status, *icon_paths)

        if new_status:
            self.load_file_content(item)
        elif not new_status:
            self.all_files_content[item.text()]['content'] = []
        self.show_file_content()

    def change_icon(self, item, status, icon_path_true, icon_path_false):
        """
        A method that changes the icon next to a file. The icon indicates which file has been selected to attach.
        """
        try:
            if not status:
                item.setIcon(QIcon(icon_path_false))
            else:
                item.setIcon(QIcon(icon_path_true))
        except Exception as e:
            print(f"Error  loading icons: {str(e)}")
            message = f"Error  loading icons: {str(e)}"
            self.show_message(message)

    def load_file_content(self, item):
        """
        A method that reads the contents of a code file, if this file has been selected for inclusion (green icon).
        The content of the file is added to the dictionary, where all indicated files (marked and unmarked) are located.
        """
        try:
            with open(self.all_files_content.get(item.text())['path'], 'r', encoding='utf-8') as file:
                self.all_files_content.get(item.text())['content'] = file.readlines()
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            message = f"Error reading file: {str(e)}"
            self.show_message(message)

    def show_file_content(self):
        """
        A method that displays the content of all selected files (with a green icon) in the editing window
        ("Joined All Files"). This content is read from the "all_files_content" dictionary.
        Thanks to this, the order of the file contents is the same as the order of files in the window for selecting them.
        """
        self.textEdit.clear()
        for file_name, file_content in self.all_files_content.items():

            if file_content['content']:
                path = file_content["path"]
                self.textEdit.insertPlainText(f"==================== \n")
                self.textEdit.insertPlainText(f"FILE: {path} \n\n")
                content_str = ''.join(file_content['content'])
                self.textEdit.insertPlainText(content_str + '\n\n')

    def join_files(self):
        """
        A method that, after clicking the "JOIN" button, saves (using a dialog box) a file with the contents of
        all selected (green icon) files.
        Additionally, if the "with layout" checkbox is checked, a file with the "all_files_content" dictionary is saved
        using the dialog box for later restoration and continuation of work.
        """
        joined_text = ''
        for file_name, file_content in self.all_files_content.items():
            path = file_content["path"]
            if file_content['content']:
                joined_text += f"==================== \n"
                joined_text += f"FILE: {path} \n\n{''.join(file_content['content'])} \n\n"
                print(joined_text)

        save_file_dialog = SaveFileDialog()
        if self.checkBox.isChecked():
            save_file_dialog.set_file_path(joined_text, self.all_files_content)
        else:
            save_file_dialog.set_file_path(joined_text, None)

    def clear_list_of_files(self):
        self.listWidget.clear()
        self.textEdit.clear()
        self.all_files_content = {}
        self.status_item = {}

    def read_files_layout(self, file_name):
        """
        A method that reads the contents of a file with the .layout extension and recreates the file layout in the file
        selection window (icons and file statuses that were marked and deselected at the time of saving).
        Based on it, the contents of the file with the combined content are recreated.

        Recreating the layout uses JSON
        """
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                files_layout = json.load(file)
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            message = f"Error reading file: {str(e)}"
            self.show_message(message)

        for key in files_layout.keys():
            item = QtWidgets.QListWidgetItem(key)
            if files_layout[key]["content"]:
                item.setIcon(QIcon("green_checkmark.png"))
            else:
                item.setIcon(QIcon("red_checkmark.png"))
            self.listWidget.addItem(item)
        return files_layout

    def is_text_file(self, filename):
        mime = magic.Magic(mime=True)
        filetype = mime.from_file(filename)
        return filetype.startswith('text/')

    def show_message(self, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle("Warning")
        msgbox.setText(message)
        msgbox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FilesJoiner()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
