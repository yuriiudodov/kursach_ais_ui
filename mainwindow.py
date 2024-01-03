# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow

import licenses_view
import main_menu_refined
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from main_menu import Ui_Widget
from parameters import create_new_order


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = QMainWindow()
        self.ui = main_menu_refined.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    #widget.show()
    sys.exit(app.exec())
