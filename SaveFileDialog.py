import sys
import json
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QMessageBox)


class SaveFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    def set_file_path(self, joined_text, all_files_content):
        default_name = "full.cr.txt"
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Joined File", default_name, "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(joined_text)
                if all_files_content:
                    file_name_conf = Path(file_name).with_suffix('.layout')
                    with open(file_name_conf, 'w') as layout_file:
                        layout_file.write(json.dumps(all_files_content))
            except Exception as e:
                print(f"Error saving file: {str(e)}")
                message = f"Error saving file: {str(e)}"
                self.show_message(message)

    def show_message(self, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle("Warning")
        msgbox.setText(message)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    ex = SaveFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
