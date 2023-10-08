import sys
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)


class SaveFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    def set_file_path(self, joined_text):  # , file_type='*'
        # home_dir = str(Path.home())
        # filter = f"{file_type.upper()} files (*.{file_type});;All Files (*)"
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Joined File", "", "Text Files (*.txt);;All Files (*)")  # , options=options
        if file_name:
            with open(file_name, 'w') as file:
                file.write(joined_text)


def main():
    app = QApplication(sys.argv)
    ex = SaveFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
