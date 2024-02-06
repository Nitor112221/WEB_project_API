import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from data.ui_py_design.main_ui import UiMainWindow


class MainApplication(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('API Application')
        self.setFixedSize(self.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApplication()
    ex.show()
    sys.exit(app.exec())
