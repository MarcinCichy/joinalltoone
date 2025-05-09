import os
import sys
import json
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox


class SaveFileDialog(QMainWindow):

    def __init__(self):
        super().__init__()

    def get_absolute_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def set_file_path(self, joined_text, all_files_content):
        default_name = "full.cr.txt"
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Joined File",
            default_name,
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                # ← tu dodane encoding='utf-8'
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(joined_text)

                if all_files_content:
                    base_path = Path(file_name).parent
                    layout_file_path = base_path / f"{Path(file_name).stem}.layout"

                    # ← i tu encoding='utf-8'
                    with open(layout_file_path, 'w', encoding='utf-8') as layout_file:
                        layout_file.write(json.dumps(all_files_content, indent=4))

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
