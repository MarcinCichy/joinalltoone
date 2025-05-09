import sys
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox


class OpenFileDialog(QMainWindow):

    def __init__(self):
        super().__init__()

    def get_file_path(self, file_types=None):
        """
        file_types:
          - None lub []     -> ['py'] (domyślnie pokazuje tylko .py)
          - str             -> traktuje jako pojedyncze rozszerzenie, np. 'py'
          - lista strów     -> np. ['py','txt','json','html','css', 'layout']
        Zwraca listę wybranych ścieżek.
        """
        try:
            home_dir = str(Path.home())

            # 1) Przygotuj listę rozszerzeń
            if not file_types:
                exts = ['py']
            elif isinstance(file_types, str):
                exts = [file_types]
            else:
                exts = list(file_types)

            # 2) Primary filter (domyślnie .py jeśli jest na liście)
            # primary = 'py' if 'py' in exts else exts[0]
            # primary_filter = f"{primary.upper()} files (*.{primary})"
            primary = exts[0]
            primary_filter = f"{primary.capitalize()} files (*.{primary})"

            # 3) Supported files (wszystkie podane rozszerzenia)
            supported_pattern = ' '.join(f"*.{e}" for e in exts)
            supported_filter  = f"Supported files ({supported_pattern})"

            # 4) All files
            all_filter = "All Files (*)"

            # scal wszystko w jeden string
            filter_str = ";;".join([primary_filter, supported_filter, all_filter])

            # otwórz dialog
            file_names, _ = QFileDialog.getOpenFileNames(
                self,
                "Open file",
                home_dir,
                filter_str
            )
            return file_names

        except Exception as e:
            print(f"Error reading file: {e}")
            self.show_message(str(e))

    def show_message(self, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle("Warning")
        msgbox.setText(message)
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    dlg = OpenFileDialog()

    # TEST domyślnie .py
    print(dlg.get_file_path())

    # TEST wszystkie typy
    print(dlg.get_file_path(['py','txt','json','html','css','layout']))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
