import sys
import json
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)


class SaveFileDialog (QMainWindow):

    def __init__(self):
        super().__init__()

    def set_file_path(self, joined_text, all_files_content):  # , file_type='*'
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Joined File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(joined_text)
                if all_files_content:
                    file_name_conf = Path(file_name).stem
                    with open(file_name_conf + '.layout', 'w') as file_name_conf:
                        file_name_conf.write(json.dumps(all_files_content))
            except Exception as e:
                print(f"Error saving file: {str(e)}")


def main():
    app = QApplication(sys.argv)
    ex = SaveFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
