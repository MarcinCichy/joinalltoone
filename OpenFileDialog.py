import sys
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QMessageBox)


class OpenFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    def get_file_path(self, file_type='*'):
        try:
            home_dir = str(Path.home())
            filter = f"{file_type.upper()} files (*.{file_type});;All Files (*)"
            file_names, _ = QFileDialog.getOpenFileNames(self, 'Open file', home_dir, filter)
            return file_names
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            message = f"Error reading file: {str(e)}"
            self.show_message(message)

    def show_message(self, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle("Warning")
        msgbox.setText(message)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    ex = OpenFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
