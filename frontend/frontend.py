import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from data.ui_py_design.main_ui import UiMainWindow
import backend.backend as backend
from PyQt5.QtCore import Qt


class MainApplication(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('API Application')
        self.setFixedSize(self.size())
        self.delta = 0.002
        self.shift_x = self.delta
        self.shift_y = self.delta
        self.update_map()

    def update_map(self):
        pixmap = backend.get_map(lon="37.530887", lat="55.703118", delta=str(self.delta))
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.delta -= 0.0005
        elif event.key() == Qt.Key_PageDown:
            self.delta += 0.0005
        self.delta = min(1., max(0., self.delta))
        self.update_map()

        if event.key() == Qt.Key_Down:
            pass
        elif event.key() == Qt.Key_Up:
            pass
        elif event.key() == Qt.Key_Left:
            pass
        elif event.key() == Qt.Key_Right:
            pass


app = QApplication(sys.argv)
ex = MainApplication()
ex.show()
sys.exit(app.exec())
