import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from data.ui_py_design.main_ui import UiMainWindow
import backend.backend as backend


class MainApplication(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('API Application')
        self.setFixedSize(self.size())
        self.pixmap = backend.get_map(lon="37.530887", lat="55.703118", delta="0.002")
        self.label.setPixmap(self.pixmap)


app = QApplication(sys.argv)
ex = MainApplication()
ex.show()
sys.exit(app.exec())
