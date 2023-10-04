import sys
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)


class OpenFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    def get_file_path(self):
        home_dir = str(Path.home())
        filter = "Python files (*.py);;All Files (*)"
        file_names, _ = QFileDialog.getOpenFileNames(self, 'Open file', home_dir, filter)
        return file_names


def main():
    app = QApplication(sys.argv)
    ex = OpenFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
