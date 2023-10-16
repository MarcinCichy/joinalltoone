import sys
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)


class OpenFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    try:
        def get_file_path(self, file_type='*'):
            home_dir = str(Path.home())
            filter = f"{file_type.upper()} files (*.{file_type});;All Files (*)"
            file_names, _ = QFileDialog.getOpenFileNames(self, 'Open file', home_dir, filter)
            return file_names
    except Exception as e:
        print(f"Error reading file: {str(e)}")


def main():
    app = QApplication(sys.argv)
    ex = OpenFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
