import sys
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QMessageBox)


class OpenDirectoryDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    def get_directory_path(self):
        try:
            home_dir = str(Path.home())
            directory = QFileDialog.getExistingDirectory(self, 'Select Directory', home_dir)
            if directory:
                return Path(directory).name
            return ""
        except Exception as e:
            print(f"Error reading directory: {str(e)}")
            message = f"Error reading directory: {str(e)}"
            self.show_message(message)

    def show_message(self, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle("Warning")
        msgbox.setText(message)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    ex = OpenDirectoryDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()