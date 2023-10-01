from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
import sys
from pathlib import Path


class OpenFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

        # open dialog
        home_dir = str(Path.home())
        QFileDialog.getOpenFileName(self, 'Open file', home_dir)



def main():
    app = QApplication(sys.argv)
    ex = OpenFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
